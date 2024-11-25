import 'package:flutter/material.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Dashboard")),
      body: LayoutBuilder(
        builder: (context, constraints) {
          if (constraints.maxWidth > 600) {
            // Layout for larger screens (tablet/desktop)
            return Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // First widget - for example, a card or box
                Expanded(
                  child: Container(
                    padding: EdgeInsets.all(16),
                    color: Colors.blue,
                    height: 200,
                    child: Center(
                      child: Text(
                        'Widget 1',
                        style: TextStyle(color: Colors.white, fontSize: 18),
                      ),
                    ),
                  ),
                ),
                SizedBox(width: 16), // Space between widgets
                // Second widget
                Expanded(
                  child: Container(
                    padding: EdgeInsets.all(16),
                    color: Colors.green,
                    height: 200,
                    child: Center(
                      child: Text(
                        'Widget 2',
                        style: TextStyle(color: Colors.white, fontSize: 18),
                      ),
                    ),
                  ),
                ),
              ],
            );
          } else {
            // Layout for smaller screens (e.g., mobile phones)
            return Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // First widget
                Container(
                  padding: EdgeInsets.all(16),
                  color: Colors.blue,
                  height: 200,
                  child: Center(
                    child: Text(
                      'Widget 1',
                      style: TextStyle(color: Colors.white, fontSize: 18),
                    ),
                  ),
                ),
                SizedBox(height: 16), // Space between widgets
                // Second widget
                Container(
                  padding: EdgeInsets.all(16),
                  color: Colors.green,
                  height: 200,
                  child: Center(
                    child: Text(
                      'Widget 2',
                      style: TextStyle(color: Colors.white, fontSize: 18),
                    ),
                  ),
                ),
              ],
            );
          }
        },
      ),
    );
  }
}

