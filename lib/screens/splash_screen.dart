import 'package:flutter/material.dart';
import 'dart:async';
import '../utils/constants.dart';

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Future.delayed(Duration(seconds: 3), () {
      Navigator.pushReplacementNamed(context, '/login');
    });

    return Scaffold(
      backgroundColor: Constants.primaryColor,
      body: Center(
        child: Text(
          Constants.appTitle,
          style: Constants.headingStyle,
        ),
      ),
    );
  }
}
