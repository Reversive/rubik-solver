from arguments.parser import parser

if __name__ == '__main__':
    args = parser.parse_args()
    print('options: ', args.options)