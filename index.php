<!DOCTYPE html>
<html>
<head>
    <title>One Pixel Attack</title>
</head>
<body>
    <h2>Upload Image for One Pixel Attack</h2>
    <form action="index.php" method="POST" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <button type="submit" name="submit">Upload & Attack</button>
    </form>

<?php
if (isset($_POST['submit'])) {
    $target_dir = "upload/";
    $output_dir = "output/";
    $filename = basename($_FILES["image"]["name"]);
    $target_file = $target_dir . $filename;
    $output_file = $output_dir . "attacked_" . $filename;

    if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
        $command = escapeshellcmd("python attack.py $target_file $output_file");
        $output = shell_exec($command);

        echo "<h3>Original Image:</h3>";
        echo "<img src='$target_file' width='300'><br>";

        if (file_exists($output_file)) {
            echo "<h3>Attacked Image:</h3>";
            echo "<img src='$output_file' width='300'><br>";
            echo "<a href='$output_file' download>Download Attacked Image</a>";
        } else {
            echo "<p style='color:red;'>Failed to generate attacked image.</p>";
            echo "<pre>$output</pre>";
        }
    } else {
        echo "<p>Failed to upload file.</p>";
    }
}
?>
</body>
</html>
