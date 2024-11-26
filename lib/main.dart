import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// Screens
import 'screens/message_screen.dart';
import 'screens/progress_screen.dart';
import 'screens/schedule_screen.dart';
import 'screens/login_screen.dart';
import 'screens/dashboard_screen.dart';

// Providers
import 'services/auth_provider.dart';

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
      create: (context) => AuthProvider(),
      child: Consumer<AuthProvider>(
        builder: (context, authProvider, child) {
          return MaterialApp(
            debugShowCheckedModeBanner: false,
            title: 'Parent-Teacher Communication',
            theme: ThemeData(
              primarySwatch: Colors.blue,
            ),
            initialRoute: authProvider.isLoggedIn ? '/dashboard' : '/login', 
            routes: {
              '/login': (context) => const LoginScreen(),
              '/dashboard': (context) => const DashboardScreen(),
              '/messages': (context) => const MessageScreen(),
              '/progress': (context) => const ProgressScreen(),
              '/schedule': (context) => const ScheduleScreen(),
            },
          );
        },
      ),
    );
  }
}
