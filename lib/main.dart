import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// Screens
import 'screens/message_screen.dart';
import 'screens/progress_screen.dart';
import 'screens/schedule_screen.dart';
import 'screens/login_screen.dart';
import 'screens/dashboard_screen.dart';
import 'screens/splash_screen.dart';
import 'screens/media_query_screen.dart';

// Providers
import 'services/auth_provider.dart';

// Utilities
import 'utils/constants.dart';

// Main entry point of the app
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      // Provide AuthProvider to the app
      create: (context) {
        final authProvider = AuthProvider();
        authProvider.checkLoginStatus();
        return authProvider;
      },
      child: Consumer<AuthProvider>(
        builder: (context, authProvider, child) {
          return MaterialApp(
            debugShowCheckedModeBanner: false,
            title: 'Parent-Teacher Communication',
            theme: appTheme, // Apply global theme
            initialRoute: '/splash', // Set Splash Screen as initial route
            onGenerateRoute: (settings) {
              // Secure routing logic
              if (!authProvider.isLoggedIn && settings.name != '/login' && settings.name != '/splash') {
                return MaterialPageRoute(builder: (context) => const LoginScreen());
              }

              switch (settings.name) {
                case '/splash':
                return MaterialPageRoute(builder: (context) => SplashScreen());
                case '/login':
                  return MaterialPageRoute(builder: (context) => const LoginScreen());
                case '/dashboard':
                  return MaterialPageRoute(builder: (context) => const DashboardScreen());
                case '/messages':
                  return MaterialPageRoute(builder: (context) => const MessageScreen());
                case '/progress':
                  return MaterialPageRoute(builder: (context) => const ProgressScreen());
                case '/schedule':
                  return MaterialPageRoute(builder: (context) => const ScheduleScreen());
                case '/responsive':  // Add the route for MediaQueryScreen
                  return MaterialPageRoute(builder: (context) => MediaQueryScreen());
                default:
                  return MaterialPageRoute(builder: (context) => const LoginScreen());
              }
            },
          );
        },
      ),
    );
  }
}
