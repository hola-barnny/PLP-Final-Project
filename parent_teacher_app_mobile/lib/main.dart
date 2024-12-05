import 'package:flutter/material.dart';
import 'screens/login.dart';

void main() {
  runApp(ParentTeacherApp());
}

class ParentTeacherApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ClassBridge',
      theme: ThemeData(
        primaryColor: Colors.orange,
        accentColor: Colors.greenAccent,
        fontFamily: 'Arial',
      ),
      home: LoginScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
