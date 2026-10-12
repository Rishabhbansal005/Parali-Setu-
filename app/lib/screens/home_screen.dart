import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import '../constants.dart';
import '../l10n/app_strings.dart';
import '../models/user_profile.dart';
import '../repositories/farmer_repository.dart';
import '../theme.dart';
import 'field_details_screen.dart';
import 'phone_login_screen.dart';

class HomeScreen extends StatefulWidget {
  final FarmerRepository repository;
  final Function(AppLanguage) onLanguageChanged;
  final AppLanguage currentLanguage;
  final bool isOffline;

  const HomeScreen({
    super.key,
    required this.repository,
    required this.onLanguageChanged,
    required this.currentLanguage,
    this.isOffline = false,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedTabIndex = 0;
  UserProfile? _profile;
  bool _isLoadingProfile = true;
  late AppLanguage _currentLanguage;
  final FlutterSecureStorage _storage = const FlutterSecureStorage();

  @override
  void initState() {
    super.initState();
    _currentLanguage = widget.currentLanguage;
    _loadProfile();
  }

  Future<void> _loadProfile() async {
    try {
      final p = await widget.repository.getProfile();
      if (mounted) {
        setState(() {
          _profile = p;
          if (p.language.isNotEmpty) {
            _currentLanguage = AppLanguage.fromCode(p.language);
          }
          _isLoadingProfile = false;
        });
      }
    } catch (_) {
      final cached = await widget.repository.getCachedProfile();
      if (mounted) {
        setState(() {
          _profile = cached;
          if (cached != null && cached.language.isNotEmpty) {
            _currentLanguage = AppLanguage.fromCode(cached.language);
          }
          _isLoadingProfile = false;
        });
      }
    }
  }

  Future<void> _handleLogout() async {
    await widget.repository.clearSession();
    if (!mounted) return;
    Navigator.pushAndRemoveUntil(
      context,
      MaterialPageRoute(
        builder: (_) => PhoneLoginScreen(
          repository: widget.repository,
          onLanguageChanged: widget.onLanguageChanged,
          currentLanguage: _currentLanguage,
        ),
      ),
      (route) => false,
    );
  }

  void _onLanguageSelected(AppLanguage lang) async {
    setState(() {
      _currentLanguage = lang;
    });
    widget.onLanguageChanged(lang);
    try {
      await _storage.write(key: AppConstants.keyLanguage, value: lang.code);
    } catch (_) {}
    try {
      final updated = await widget.repository.updateProfile(language: lang.code);
      if (mounted) {
        setState(() => _profile = updated);
      }
    } catch (_) {}
  }

  void _showNotificationCenter() {
    final displayName = _profile?.name ?? 'Gurpreet Singh';
    final alertTitle = _currentLanguage == AppLanguage.punjabi
        ? '$displayName ਦੇ ਸੁਨੇਹੇ (ਅਲਰਟ)'
        : (_currentLanguage == AppLanguage.hindi
            ? '$displayName के संदेश (अलर्ट)'
            : "$displayName's Alerts");

    final notifications = _currentLanguage == AppLanguage.punjabi
        ? [
            {
              'title': '💰 ₹12,000 ਖਾਤੇ ਵਿੱਚ ਜਮ੍ਹਾਂ (Escrow ਜਾਰੀ)',
              'body': 'ਧਰਮਕੰਡਾ ਸਕੇਲ ਨੇ 8.0t ਪਰਾਲੀ ਦੀ ਪੁਸ਼ਟੀ ਕੀਤੀ। ਭੁਗਤਾਨ IMPS ਰਾਹੀਂ ਸਫਲਤਾਪੂਰਵਕ ਜਮ੍ਹਾਂ ਹੋਇਆ।',
              'time': 'ਹੁਣੇ',
              'icon': Icons.account_balance_wallet,
              'color': AppTheme.primaryGreen,
            },
            {
              'title': '🚜 ਟਰੱਕ ਅਤੇ ਬੇਲਰ ਰਵਾਨਾ (ਟਰੱਕ ਰਵਾਨਾ)',
              'body': 'ਗੱਡੀ ਨੰਬਰ PB-11-AB-4029 ਤੁਹਾਡੇ ਖੇਤ (Kot Buddha) ਲਈ ਰਵਾਨਾ ਹੋ ਚੁੱਕੀ ਹੈ। ETA: 25 ਮਿੰਟ।',
              'time': '15 ਮਿੰਟ ਪਹਿਲਾਂ',
              'icon': Icons.local_shipping,
              'color': Colors.blue,
            },
            {
              'title': '🛰️ ਨੋ-ਬਰਨ ਸਰਟੀਫਿਕੇਟ ਜਾਰੀ (Sentinel-2)',
              'body': 'Sentinel-2 ਸੈਟੇਲਾਈਟ ਨੇ ਜ਼ੀਰੋ ਅੱਗ ਦੀ ਪੁਸ਼ਟੀ ਕੀਤੀ (dNBR 0.038)। ₹2,500/ਏਕੜ ਸਬਸਿਡੀ ਅਨਲੌਕ।',
              'time': '1 ਘੰਟਾ ਪਹਿਲਾਂ',
              'icon': Icons.verified,
              'color': Colors.purple,
            },
          ]
        : (_currentLanguage == AppLanguage.hindi
            ? [
                {
                  'title': '💰 ₹12,000 खाते में जमा (एस्क्रो रिलीज)',
                  'body': 'धर्मकांटा स्केल ने 8.0t पराली सत्यापित की। भुगतान IMPS द्वारा सफलतापूर्वक जमा हुआ।',
                  'time': 'अभी',
                  'icon': Icons.account_balance_wallet,
                  'color': AppTheme.primaryGreen,
                },
                {
                  'title': '🚜 ट्रक और बेलर रवाना (ट्रक प्रेषित)',
                  'body': 'गाड़ी संख्या PB-11-AB-4029 आपके खेत (Kot Buddha) के लिए रवाना हो चुकी है। ETA: 25 मिनट।',
                  'time': '15 मिनट पहले',
                  'icon': Icons.local_shipping,
                  'color': Colors.blue,
                },
                {
                  'title': '🛰️ नो-बर्न सर्टिफिकेट जारी (Sentinel-2)',
                  'body': 'Sentinel-2 सैटेलाइट ने शून्य आग की पुष्टि की (dNBR 0.038)। ₹2,500/एकड़ सब्सिडी अनलॉक।',
                  'time': '1 घंटा पहले',
                  'icon': Icons.verified,
                  'color': Colors.purple,
                },
              ]
            : [
                {
                  'title': '💰 ₹12,000 Credited (Escrow Released)',
                  'body': 'Dharamkanta scale verified 8.0t stubble. Payment disbursed successfully via IMPS.',
                  'time': 'Just now',
                  'icon': Icons.account_balance_wallet,
                  'color': AppTheme.primaryGreen,
                },
                {
                  'title': '🚜 Truck & Baler Dispatched',
                  'body': 'Vehicle PB-11-AB-4029 is en route to your field (Kot Buddha). ETA: 25 mins.',
                  'time': '15m ago',
                  'icon': Icons.local_shipping,
                  'color': Colors.blue,
                },
                {
                  'title': '🛰️ No-Burn Certificate Issued (Sentinel-2)',
                  'body': 'Sentinel-2 satellite confirmed zero fire (dNBR 0.038). ₹2,500/acre subsidy unlocked.',
                  'time': '1h ago',
                  'icon': Icons.verified,
                  'color': Colors.purple,
                },
              ]);

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return Padding(
          padding: EdgeInsets.only(
            left: 20,
            right: 20,
            top: 20,
            bottom: MediaQuery.of(ctx).viewInsets.bottom + 24,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Expanded(
                    child: Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            color: AppTheme.primaryGreen.withValues(alpha: 0.12),
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(Icons.notifications_active, color: AppTheme.primaryGreen, size: 22),
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Text(
                            alertTitle,
                            style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textDark),
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.close),
                    onPressed: () => Navigator.pop(ctx),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              ...notifications.map((n) => Container(
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: const Color(0xFFF9FAF9),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: const Color(0xFFE2ECE2)),
                ),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: (n['color'] as Color).withValues(alpha: 0.12),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Icon(n['icon'] as IconData, color: n['color'] as Color, size: 20),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Expanded(
                                child: Text(
                                  n['title'] as String,
                                  style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textDark),
                                ),
                              ),
                              Text(n['time'] as String, style: const TextStyle(fontSize: 11, color: AppTheme.textMuted)),
                            ],
                          ),
                          const SizedBox(height: 4),
                          Text(
                            n['body'] as String,
                            style: const TextStyle(fontSize: 12, color: AppTheme.textMuted, height: 1.35),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              )),
            ],
          ),
        );
      },
    );
  }

  void _showEditProfileDialog() {
    final strings = AppStrings(_currentLanguage);
    final nameController = TextEditingController(text: _profile?.name ?? '');
    final villageController = TextEditingController(text: _profile?.village ?? '');
    final districtController = TextEditingController(text: _profile?.district ?? '');

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return Padding(
          padding: EdgeInsets.only(
            left: 24,
            right: 24,
            top: 24,
            bottom: MediaQuery.of(ctx).viewInsets.bottom + 24,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                strings.edit,
                style: const TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textDark,
                ),
              ),
              const SizedBox(height: 18),
              TextField(
                controller: nameController,
                decoration: InputDecoration(
                  labelText: strings.nameLabel,
                ),
              ),
              const SizedBox(height: 14),
              TextField(
                controller: villageController,
                decoration: const InputDecoration(
                  labelText: 'Village',
                ),
              ),
              const SizedBox(height: 14),
              TextField(
                controller: districtController,
                decoration: const InputDecoration(
                  labelText: 'District',
                ),
              ),
              const SizedBox(height: 16),
              Text(
                strings.chooseLanguage,
                style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppTheme.textDark),
              ),
              const SizedBox(height: 8),
              Row(
                children: [
                  ChoiceChip(
                    label: Text(strings.englishLabel),
                    selected: _currentLanguage == AppLanguage.english,
                    onSelected: (_) {
                      _onLanguageSelected(AppLanguage.english);
                      Navigator.pop(ctx);
                    },
                  ),
                  const SizedBox(width: 8),
                  ChoiceChip(
                    label: const Text('हिंदी'),
                    selected: _currentLanguage == AppLanguage.hindi,
                    onSelected: (_) {
                      _onLanguageSelected(AppLanguage.hindi);
                      Navigator.pop(ctx);
                    },
                  ),
                  const SizedBox(width: 8),
                  ChoiceChip(
                    label: const Text('ਪੰਜਾਬੀ'),
                    selected: _currentLanguage == AppLanguage.punjabi,
                    onSelected: (_) {
                      _onLanguageSelected(AppLanguage.punjabi);
                      Navigator.pop(ctx);
                    },
                  ),
                ],
              ),
              const SizedBox(height: 24),
              SizedBox(
                height: 56,
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: () async {
                    Navigator.pop(ctx);
                    try {
                      final updated = await widget.repository.updateProfile(
                        name: nameController.text.trim(),
                        village: villageController.text.trim(),
                        district: districtController.text.trim(),
                      );
                      setState(() => _profile = updated);
                    } catch (e) {
                      if (!mounted) return;
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text(e.toString())),
                      );
                    }
                  },
                  child: Text(strings.save),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final strings = AppStrings(_currentLanguage);

    return Scaffold(
      backgroundColor: AppTheme.warmBackground,
      body: SafeArea(
        child: Column(
          children: [
            // Small offline banner if running without network
            if (widget.isOffline)
              Container(
                width: double.infinity,
                color: Colors.amber.shade700,
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: Row(
                  children: [
                    const Icon(Icons.cloud_off, color: Colors.white, size: 18),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        strings.offlineBanner,
                        style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w600),
                      ),
                    ),
                  ],
                ),
              ),

            Expanded(
              child: _selectedTabIndex == 0 ? _buildHomeTab(strings) : _buildProfileTab(strings),
            ),
          ],
        ),
      ),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          color: Colors.white,
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.05),
              blurRadius: 10,
              offset: const Offset(0, -3),
            ),
          ],
        ),
        child: BottomNavigationBar(
          currentIndex: _selectedTabIndex,
          onTap: (idx) => setState(() => _selectedTabIndex = idx),
          backgroundColor: Colors.white,
          selectedItemColor: AppTheme.primaryGreen,
          unselectedItemColor: AppTheme.textMuted,
          selectedFontSize: 14,
          unselectedFontSize: 14,
          elevation: 0,
          items: [
            BottomNavigationBarItem(
              icon: const Icon(Icons.home_outlined),
              activeIcon: const Icon(Icons.home),
              label: strings.homeTab,
            ),
            BottomNavigationBarItem(
              icon: const Icon(Icons.person_outline),
              activeIcon: const Icon(Icons.person),
              label: strings.profileTab,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHomeTab(AppStrings strings) {
    final displayName = _profile?.name ?? (_isLoadingProfile ? '...' : 'Farmer');

    return SingleChildScrollView(
      padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Greeting with user name
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      strings.welcomeFarmer(displayName),
                      style: const TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.bold,
                        color: AppTheme.textDark,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      strings.tagline,
                      style: const TextStyle(
                        fontSize: 14,
                        color: AppTheme.textMuted,
                      ),
                    ),
                  ],
                ),
              ),
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  IconButton(
                    icon: Stack(
                      clipBehavior: Clip.none,
                      children: [
                        const Icon(Icons.notifications_outlined, color: AppTheme.primaryGreen, size: 28),
                        Positioned(
                          right: -2,
                          top: -2,
                          child: Container(
                            padding: const EdgeInsets.all(4),
                            decoration: const BoxDecoration(
                              color: Colors.red,
                              shape: BoxShape.circle,
                            ),
                            child: const Text('3', style: TextStyle(color: Colors.white, fontSize: 9, fontWeight: FontWeight.bold)),
                          ),
                        ),
                      ],
                    ),
                    onPressed: _showNotificationCenter,
                  ),
                  const SizedBox(width: 4),
                  GestureDetector(
                    onTap: () => setState(() => _selectedTabIndex = 1),
                    child: CircleAvatar(
                      radius: 22,
                      backgroundColor: AppTheme.primaryGreen.withValues(alpha: 0.12),
                      child: const Icon(Icons.person, color: AppTheme.primaryGreen, size: 26),
                    ),
                  ),
                ],
              ),
            ],
          ),

          // Weather & Ambient Harvest banner (Matching reference design)
          Container(
            margin: const EdgeInsets.only(top: 14, bottom: 18),
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: const Color(0xFFF1F8F1),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: const Color(0xFFCDE4CD)),
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.amber.shade100,
                    shape: BoxShape.circle,
                  ),
                  child: const Icon(Icons.wb_sunny_rounded, color: Colors.amber, size: 20),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        _currentLanguage == AppLanguage.punjabi
                            ? '28°C · ਧੁੱਪ · ਤਰਨ ਤਾਰਨ ਹੱਬ'
                            : (_currentLanguage == AppLanguage.hindi
                                ? '28°C · धूप · तरनतारन हब'
                                : '28°C · Sunny · Tarn Taran Hub'),
                        style: const TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.bold,
                          color: AppTheme.textDark,
                        ),
                      ),
                      Text(
                        _currentLanguage == AppLanguage.punjabi
                            ? 'ਬੇਲਿੰਗ ਅਤੇ ਪਰਾਲੀ ਇਕੱਠੀ ਕਰਨ ਲਈ ਉੱਤਮ ਮੌਸਮ'
                            : (_currentLanguage == AppLanguage.hindi
                                ? 'बेलिंग और पराली संग्रहण हेतु अनुकूल मौसम'
                                : 'Ideal conditions for baling & residue collection'),
                        style: TextStyle(
                          fontSize: 11,
                          color: Colors.grey.shade700,
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: AppTheme.primaryGreen.withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    _currentLanguage == AppLanguage.punjabi
                        ? 'ਖ਼ਰੀਫ਼ 26'
                        : (_currentLanguage == AppLanguage.hindi
                            ? 'खरीफ 26'
                            : 'Kharif 26'),
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.primaryGreen,
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Primary Hero Card: "Check my stubble value"
          Card(
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
            elevation: 4,
            shadowColor: AppTheme.primaryGreen.withValues(alpha: 0.2),
            child: Container(
              padding: const EdgeInsets.all(22),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(24),
                gradient: const LinearGradient(
                  colors: [
                    Color(0xFF0F3E15),
                    AppTheme.primaryGreen,
                    Color(0xFF2E7D32),
                  ],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                boxShadow: [
                  BoxShadow(
                    color: AppTheme.primaryGreen.withValues(alpha: 0.15),
                    blurRadius: 16,
                    offset: const Offset(0, 8),
                  ),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                        decoration: BoxDecoration(
                          color: AppTheme.wheatGold,
                          borderRadius: BorderRadius.circular(10),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withValues(alpha: 0.1),
                              blurRadius: 4,
                              offset: const Offset(0, 2),
                            ),
                          ],
                        ),
                        child: Text(
                          strings.tonnesUnit,
                          style: const TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: Colors.white.withValues(alpha: 0.12),
                          shape: BoxShape.circle,
                        ),
                        child: const Icon(Icons.currency_rupee, color: Colors.white, size: 22),
                      ),
                    ],
                  ),
                  const SizedBox(height: 18),
                  Text(
                    strings.checkStubbleCardTitle,
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      height: 1.25,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    strings.checkStubbleCardSubtitle,
                    style: TextStyle(
                      fontSize: 14,
                      color: Colors.white.withValues(alpha: 0.9),
                      height: 1.35,
                    ),
                  ),

                  // Voice intake feature chip
                  Container(
                    margin: const EdgeInsets.only(top: 14, bottom: 18),
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: Colors.white.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: Colors.white.withValues(alpha: 0.2)),
                    ),
                    child: const Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.mic, color: Colors.amber, size: 16),
                        SizedBox(width: 6),
                        Text(
                          'Voice Intake Ready (ਪੰਜਾਬੀ / हिंदी)',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),

                  SizedBox(
                    height: 56,
                    width: double.infinity,
                    child: ElevatedButton(
                      key: const Key('check_stubble_btn'),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppTheme.wheatGold,
                        foregroundColor: Colors.white,
                        elevation: 2,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(16),
                        ),
                      ),
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => FieldDetailsScreen(
                              repository: widget.repository,
                              onLanguageChanged: widget.onLanguageChanged,
                              currentLanguage: widget.currentLanguage,
                            ),
                          ),
                        );
                      },
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            strings.estimateNowBtn,
                            style: const TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(width: 8),
                          const Icon(Icons.arrow_forward, size: 20),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),

          const SizedBox(height: 28),

          // "How it works" Strip
          Text(
            strings.howItWorksHeading,
            style: const TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: AppTheme.textDark,
            ),
          ),
          const SizedBox(height: 14),

          _buildStepCard(
            stepNumber: '1',
            icon: Icons.edit_location_alt_outlined,
            title: strings.step1Title,
            subtitle: strings.step1Desc,
          ),
          const SizedBox(height: 10),
          _buildStepCard(
            stepNumber: '2',
            icon: Icons.calculate_outlined,
            title: strings.step2Title,
            subtitle: strings.step2Desc,
          ),
          const SizedBox(height: 10),
          _buildStepCard(
            stepNumber: '3',
            icon: Icons.local_shipping_outlined,
            title: strings.step3Title,
            subtitle: strings.step3Desc,
          ),
        ],
      ),
    );
  }

  Widget _buildStepCard({
    required String stepNumber,
    required IconData icon,
    required String title,
    required String subtitle,
    String? badge,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFE5EDE5)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: AppTheme.primaryGreen.withValues(alpha: 0.08),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: AppTheme.primaryGreen, size: 24),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Flexible(
                      child: Text(
                        title,
                        style: const TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: AppTheme.textDark,
                        ),
                      ),
                    ),
                    if (badge != null) ...[
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: Colors.amber.shade100,
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          badge,
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.bold,
                            color: Colors.amber.shade900,
                          ),
                        ),
                      ),
                    ],
                  ],
                ),
                const SizedBox(height: 3),
                Text(
                  subtitle,
                  style: const TextStyle(
                    fontSize: 13,
                    color: AppTheme.textMuted,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildProfileTab(AppStrings strings) {
    return SingleChildScrollView(
      padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            strings.profileHeading,
            style: const TextStyle(
              fontSize: 26,
              fontWeight: FontWeight.bold,
              color: AppTheme.textDark,
            ),
          ),
          const SizedBox(height: 20),

          // Name Card (Editable)
          Card(
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 8),
              leading: const Icon(Icons.person, color: AppTheme.primaryGreen, size: 28),
              title: Text(strings.nameLabel, style: const TextStyle(fontSize: 13, color: AppTheme.textMuted)),
              subtitle: Text(
                _profile?.name ?? strings.notSpecified,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.textDark),
              ),
              trailing: IconButton(
                icon: const Icon(Icons.edit, color: AppTheme.primaryGreen),
                onPressed: _showEditProfileDialog,
              ),
            ),
          ),

          const SizedBox(height: 12),

          // Phone Card (Read-only)
          Card(
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 8),
              leading: const Icon(Icons.phone, color: AppTheme.primaryGreen, size: 28),
              title: Text(strings.phoneLabel, style: const TextStyle(fontSize: 13, color: AppTheme.textMuted)),
              subtitle: Text(
                _profile?.phone ?? '',
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.textDark),
              ),
            ),
          ),

          const SizedBox(height: 12),

          // Village & District
          Card(
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 8),
              leading: const Icon(Icons.location_on, color: AppTheme.primaryGreen, size: 28),
              title: Text(strings.villageDistrictLabel, style: const TextStyle(fontSize: 13, color: AppTheme.textMuted)),
              subtitle: Text(
                '${_profile?.village ?? "Bhikhiwind"}, ${_profile?.district ?? "Tarn Taran"}',
                style: const TextStyle(fontSize: 17, fontWeight: FontWeight.bold, color: AppTheme.textDark),
              ),
            ),
          ),

          const SizedBox(height: 20),

          // Language Selector
          Text(
            strings.chooseLanguage,
            style: const TextStyle(
              fontSize: 17,
              fontWeight: FontWeight.bold,
              color: AppTheme.textDark,
            ),
          ),
          const SizedBox(height: 10),
          Row(
            children: [
              _buildLangChip(strings.englishLabel, AppLanguage.english),
              const SizedBox(width: 8),
              _buildLangChip('हिंदी', AppLanguage.hindi),
              const SizedBox(width: 8),
              _buildLangChip('ਪੰਜਾਬੀ', AppLanguage.punjabi),
            ],
          ),

          const SizedBox(height: 16),

          // Logout Button
          SizedBox(
            height: 56,
            width: double.infinity,
            child: OutlinedButton(
              style: OutlinedButton.styleFrom(
                foregroundColor: AppTheme.warningRed,
                side: const BorderSide(color: AppTheme.warningRed, width: 1.5),
              ),
              onPressed: _handleLogout,
              child: Text(strings.logout),
            ),
          ),
          const SizedBox(height: 24),
        ],
      ),
    );
  }

  Widget _buildLangChip(String label, AppLanguage lang) {
    final isSelected = _currentLanguage == lang;
    return ChoiceChip(
      label: Text(
        label,
        style: TextStyle(
          fontSize: 14,
          fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
          color: isSelected ? Colors.white : AppTheme.textDark,
        ),
      ),
      selected: isSelected,
      selectedColor: AppTheme.primaryGreen,
      backgroundColor: Colors.white,
      side: BorderSide(color: isSelected ? AppTheme.primaryGreen : const Color(0xFFD0DDD0)),
      onSelected: (_) => _onLanguageSelected(lang),
    );
  }
}
