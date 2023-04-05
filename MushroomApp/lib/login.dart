import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Login'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                controller: _emailController,
                decoration: InputDecoration(
                  labelText: 'Email',
                ),
              ),
              SizedBox(height: 16),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: 'Password',
                ),
              ),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  // TODO: handle login logic
                },
                child: Text('Login'),
              ),
              TextButton(
                onPressed: () {
                  // TODO: handle forgot password logic
                },
                child: Text('Forgot password?'),
              ),
              TextButton(
                onPressed: () {
                  // TODO: navigate to registration screen
                },
                child: Text('Register'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
