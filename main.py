from image import *
from docopt import docopt


usage = '''

Image Manipulation
Usage:  main.py (-l <input_file> -p <position>) (-o <output_file>) [(-t <text>)]
        main.py (-i <input_file> -T <text>) (-o <output_file>)
        main.py (--logo <input_file> --position <position>) --output <output_file>
        main.py (-h | --help)


Examples:

    Add a logo of sponsor on the input image

    main.py -l logos/sponsor.png -p bcl -o parth
    main.py --logo logos/sponsor.png --position bcl --output parth

    Add logo with text

    main.py -l logos/sponsor.png -p bcl -o parth -t GCS2020

Positions - Watermark:
        tl      Top Left Corner
        b       Below Watermark Image
        tc      Top Center
        r       On Right Of Watermark Image
        tr      Top Right
        cl      Center Left
        c       Center 
        cr      Center Right
        bl      Bottom Left
        bc      Bottom Center
        br      Bottom Right 
        bcl     Bottom Center Left

Positions - Watermark With Text:
        tl      Top Left Corner
        tc      Top Center
        tr      Top Right
        cl      Center Left
        c       Center 
        cr      Center Right
        bl      Bottom Left
        bc      Bottom Center
        br      Bottom Right 

'''


def main():
    args = docopt(usage, version='Image Manipulation v1')
    if args['-l' and '-p' and '-o' ]:
        logo = str(args['<input_file>'])
        position = str(args['<position>'])
        output_name = str(args['<output_file>'])
        OUTPUT = OUTPUT+output_name+".png"

        if args['-t']:
            text = str(args['<text>'])
            watermark(INPUT, OUTPUT, logo, position, text, color=COLOR, text_size=TEXT_SIZE, text_position=TEXT_ALIGN_WATERMARK)
        else:
            watermark(INPUT, OUTPUT, logo, position)


    elif args['-i' and '-T' and '-o']:
        image = str(args['<input_file>'])
        text = str(args['<text>'])
        output_name = str(args['<output_file>'])
        OUTPUT = OUTPUT+output_name+".png"

        if args['-p']:
            position = str(args['<position>'])
            watermark_with_text(image, OUTPUT, text, position, color=COLOR, text_size=TEXT_SIZE)
        else:
            watermark_with_text(image, OUTPUT, text, text_position=TEXT_POSITION, color=COLOR, text_size=TEXT_SIZE)


if __name__ == '__main__':
    main()

