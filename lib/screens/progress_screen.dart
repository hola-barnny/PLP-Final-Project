import 'package:flutter/material.dart';
import '../services/database_service.dart';

class ProgressScreen extends StatefulWidget {
  const ProgressScreen({Key? key}) : super(key: key);

  @override
  _ProgressScreenState createState() => _ProgressScreenState();
}

class _ProgressScreenState extends State<ProgressScreen> {
  final DatabaseService databaseService = DatabaseService();
  List<dynamic> progressData = [];
  bool isLoading = true;
  int? expandedCardIndex;

  @override
  void initState() {
    super.initState();
    fetchProgress();
  }

  void fetchProgress() async {
    try {
      final data = await databaseService.getStudentProgress('student123');
      setState(() {
        progressData = data;
        isLoading = false;
      });
    } catch (e) {
      setState(() {
        isLoading = false;
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error fetching progress: $e')),
      );
    }
  }

  void toggleExpand(int index) {
    setState(() {
      expandedCardIndex = (expandedCardIndex == index) ? null : index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student Progress'),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : Padding(
              padding: const EdgeInsets.all(16.0),
              child: ListView.builder(
                itemCount: progressData.length,
                itemBuilder: (context, index) {
                  final progress = progressData[index];
                  return _animatedProgressCard(
                    index: index,
                    isExpanded: expandedCardIndex == index,
                    subject: progress['subject'],
                    grade: progress['grade'],
                    attendance: progress['attendance'],
                    comments: progress['comments'],
                  );
                },
              ),
            ),
    );
  }

  Widget _animatedProgressCard({
    required int index,
    required bool isExpanded,
    required String subject,
    required String grade,
    required String attendance,
    required String comments,
  }) {
    return GestureDetector(
      onTap: () => toggleExpand(index),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 500),
        curve: Curves.easeInOut,
        margin: const EdgeInsets.symmetric(vertical: 8.0),
        padding: const EdgeInsets.all(12.0),
        decoration: BoxDecoration(
          color: isExpanded ? Colors.blue.shade50 : Colors.white,
          borderRadius: BorderRadius.circular(12),
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.2),
              blurRadius: 8,
              spreadRadius: 2,
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              subject,
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 5),
            Text('Grade: $grade', style: const TextStyle(fontSize: 16)),
            Text('Attendance: $attendance', style: const TextStyle(fontSize: 16)),
            if (isExpanded) ...[
              const SizedBox(height: 10),
              const Text(
                'Comments:',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(comments),
            ],
          ],
        ),
      ),
    );
  }
}
