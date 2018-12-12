import os
import xparser
import config

def handle_file( f ):
    if config.log_level >= 2:
        print("[LOG] Reading " + str(f) + ".")

    # Read preset file content.
    fo = open( os.path.join( xparser.cwd, config.presets_folder, f ), "r" )
    content = fo.read()
    
    # Replace values.
    for k, v in xparser.result.items():
        if content.find( k ) >= 0:
            content = content.replace( "${" + k + "}", v)

    fo.close()

    # Write the new config.
    # The parameter 'w+' is needed, as the file might not exist.
    fo = open( os.path.join( xparser.cwd, config.output_folder, f ), "w+" )
    fo.write(content)
    fo.close()

def init( i ):
    xparser.parse_file( i )
    
    # To make sure the necessary folders exist.
    os.system("mkdir -p " + os.path.join( xparser.cwd, config.output_folder ) + " >/dev/null")
    os.system("mkdir -p " + os.path.join( xparser.cwd, config.presets_folder ) + " >/dev/null")

    # Python's file operations do not support tilde (~), so they can be replaced with the users home directory ($HOME).
    config.presets_folder = config.presets_folder.replace( "~", os.path.expanduser("~") )
    config.output_folder = config.output_folder.replace( "~", os.path.expanduser("~") )

    for i in os.listdir( os.path.join( xparser.cwd, config.presets_folder ) ):
        handle_file( i )
