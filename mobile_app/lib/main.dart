import 'package:flutter/material.dart';
import 'screens/login.dart';
import 'package:parent_teacher_app_mobile/themes/theme.dart';
import 'package:parent_teacher_app_mobile/screens/dashboard.dart';
import 'package:parent_teacher_app_mobile/screens/messaging.dart';
import 'package:parent_teacher_app_mobile/screens/schedule.dart';

void main() {
  runApp(const ParentTeacherApp());
}

class ParentTeacherApp extends StatelessWidget {
  const ParentTeacherApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ClassBridge',
      theme: AppTheme.lightTheme,  // Ensure AppTheme is defined correctly
      darkTheme: AppTheme.darkTheme,  // Ensure AppTheme is defined correctly
      themeMode: ThemeMode.system,
      home: LoginScreen(), // Removed 'const' here since LoginScreen doesn't need 'const'
      debugShowCheckedModeBanner: false,
      routes: {
        '/login': (context) => LoginScreen(), // Removed 'const' here too
        '/dashboard': (context) => DashboardScreen(), // Removed 'const'
        '/messaging': (context) => MessagingScreen(), // Removed 'const'
        '/schedule': (context) => ScheduleScreen(), // Removed 'const'
      },
    );
  }
}
