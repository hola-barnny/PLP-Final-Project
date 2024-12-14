import 'package:flutter/material.dart';

class ScheduleScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Schedule'),
      ),
      body: Center(
        child: Text('Your upcoming meetings will appear here.'),
      ),
    );
  }
}
