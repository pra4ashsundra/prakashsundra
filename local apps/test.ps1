# Define the path to the directory
$directoryPath = "C:\Prakash Jyotisa\Varshapala\periods"

# Get the list of files in the directory
$fileNames = Get-ChildItem -Path $directoryPath -File | Select-Object -ExpandProperty Name

# Output the file names
$fileNames

