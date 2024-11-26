import 'package:flutter/material.dart';

class MediaQueryScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Get screen width and height using MediaQuery
    double screenWidth = MediaQuery.of(context).size.width;
    double screenHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(title: Text('Responsive with MediaQuery')),
      body: Center(
        child: Container(
          width: screenWidth * 0.8, // 80% of screen width
          height: screenHeight * 0.4, // 40% of screen height
          color: Colors.blue,
          child: Center(child: Text('Responsive Box')),
        ),
      ),
    );
  }
}
