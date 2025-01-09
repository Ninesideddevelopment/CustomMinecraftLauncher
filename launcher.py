import minecraft_launcher_lib as mcll
import subprocess
import sys

def launch():
	directory = mcll.utils.get_minecraft_directory()
	mcll.install.install_minecraft_version("1.21.4", directory)

	options = mcll.utils.generate_test_options() #REMOVE WHEN PUBLISHING

	minecraft_command = mcll.command.get_minecraft_command("1.21.4", directory, options)

	print(minecraft_command)
	subprocess.run(minecraft_command)