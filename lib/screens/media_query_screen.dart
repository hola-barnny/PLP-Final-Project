import 'package:flutter/material.dart';
import '../utils/constants.dart'; // Import Constants for consistency

class MediaQueryScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Get screen width and height using MediaQuery
    double screenWidth = MediaQuery.of(context).size.width;
    double screenHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Constants.primaryColor, // Use app-wide primary color
        title: Text(
          'Responsive with MediaQuery',
          style: Constants.headingStyle, // Use consistent heading style
        ),
      ),
      body: Center(
        child: Container(
          width: screenWidth * 0.8, // 80% of screen width
          height: screenHeight * 0.4, // 40% of screen height
          decoration: BoxDecoration(
            color: Constants.primaryColor, // Use app-wide primary color
            borderRadius: BorderRadius.circular(16), // Rounded corners
          ),
          child: Center(
            child: Text(
              'Responsive Box',
              style: Constants.subtitleStyle.copyWith(
                color: Colors.white, // Make text stand out on the blue background
              ),
            ),
          ),
        ),
      ),
    );
  }
}
