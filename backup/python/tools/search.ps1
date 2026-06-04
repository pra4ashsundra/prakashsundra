# Define the path to scan
$path = "G:\My Drive\client ref"

# Get all the files in the directory and subdirectories
$files = Get-ChildItem -Path $path -Recurse -File

# Loop through each file and search for the word "gem"
foreach ($file in $files) {
    # Use Select-String to find the word "gem" in the file content
    $matches = Select-String -Path $file.FullName -Pattern "Chandran - 9th" -SimpleMatch

    # If any matches are found, output the file name
    if ($matches) {
        Write-Host "Match found in file: $($file.FullName)"
    }
}
