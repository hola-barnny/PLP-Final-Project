import 'package:flutter/material.dart';
import 'screens/login.dart';

void main() {
  runApp(ParentTeacherApp());
}

class ParentTeacherApp extends StatelessWidget {
  const ParentTeacherApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ClassBridge',
      theme: ThemeData(
        primaryColor: Colors.orange,
        fontFamily: 'Arial', colorScheme: ColorScheme.fromSwatch().copyWith(secondary: Colors.greenAccent),
      ),
      home: LoginScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
