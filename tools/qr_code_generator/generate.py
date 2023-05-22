import argparse
import qrcode
import qrcode.image.svg


def main():
    parser = argparse.ArgumentParser(description="Process a given URI and output as SVG or PNG.")
    parser.add_argument("uri", help="URI to be processed.")
    parser.add_argument("-o", "--output", choices=["svg", "png"], default="png", help="Output file type, either 'svg' or 'png'. Default is 'png'.")
    parser.add_argument("-f", "--filename", help="Name of the output file (excluding extension).")
    
    args = parser.parse_args()

    process_url(args.uri, args.output, args.filename)


def process_url(target_uri, output_type, output_filename):
    if output_type == 'png':
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )

        qr.add_data(target_uri)
        qr.make(fit=True)

        img = qr.make_image()
        img.save(f'{output_filename}.png')
    
    elif output_type == 'svg':
        method = "path" # factory method [basic,fragement, path]

        if method == 'basic':
            # Simple factory, just a set of rects.
            factory = qrcode.image.svg.SvgImage
        elif method == 'fragment':
            # Fragment factory (also just a set of rects)
            factory = qrcode.image.svg.SvgFragmentImage
        elif method == 'path':
            # Combined path factory, fixes white space that may occur when zooming
            factory = qrcode.image.svg.SvgPathImage

        # Set data to qrcode
        img = qrcode.make(target_uri, image_factory = factory)

        # Save svg file somewhere
        img.save(f"{output_filename}.svg")


if __name__ == "__main__":
    main()
