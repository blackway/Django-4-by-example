import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:sakila_flutter/providers/sakila_provider.dart';
import 'package:sakila_flutter/screens/home_screen.dart';

void main() {
  testWidgets('Home screen renders correctly', (WidgetTester tester) async {
    await tester.pumpWidget(
      ChangeNotifierProvider(
        create: (_) => SakilaProvider(),
        child: const MaterialApp(home: HomeScreen()),
      ),
    );

    expect(find.text('Sakila Movie Rental'), findsOneWidget);
    expect(find.text('Films'), findsOneWidget);
    expect(find.text('Actors'), findsOneWidget);
    expect(find.text('Categories'), findsOneWidget);
  });
}
