<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="login-container">
    <h2>Login</h2>
    <form action="submit_form.php" method="POST">
      <div class="input-box">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" required>
      </div>
      <div class="input-box">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" required>
      </div>
      <button type="submit">Login</button>
      <p class="register-link">Don't have an account? <a href="#">Register</a></p>
    </form>
  </div>
</body>
</html>
