import 'package:flutter/material.dart';
import 'media_query_screen.dart'; 

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dashboard"),
        centerTitle: true,
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          // For larger screens (tablet/desktop)
          if (constraints.maxWidth > 600) {
            return Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // Widget 1: Student Progress Card
                Expanded(
                  child: Card(
                    margin: EdgeInsets.all(16),
                    color: Colors.blue.shade100,
                    elevation: 5,
                    child: Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.school, size: 50, color: Colors.blue),
                          SizedBox(height: 10),
                          Text(
                            'Student Progress',
                            style: TextStyle(
                                fontSize: 18, fontWeight: FontWeight.bold),
                          ),
                          SizedBox(height: 10),
                          Text('View student performance and updates'),
                        ],
                      ),
                    ),
                  ),
                ),
                SizedBox(width: 16),
                // Widget 2: Messaging Card
                Expanded(
                  child: Card(
                    margin: EdgeInsets.all(16),
                    color: Colors.green.shade100,
                    elevation: 5,
                    child: Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.message, size: 50, color: Colors.green),
                          SizedBox(height: 10),
                          Text(
                            'Messages',
                            style: TextStyle(
                                fontSize: 18, fontWeight: FontWeight.bold),
                          ),
                          SizedBox(height: 10),
                          Text('Send and receive messages'),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            );
          } else {
            // For smaller screens (mobile), show the MediaQueryScreen
            return MediaQueryScreen(); // Display the MediaQueryScreen for mobile
          }
        },
      ),
    );
  }
}
