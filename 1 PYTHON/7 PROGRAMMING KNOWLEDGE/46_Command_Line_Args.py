import argparse

if __name__=="__main__":
    # initialise the parser
    parser=argparse.ArgumentParser(
        description="my python script"
    )



    # add the parameters positional/optional
    # positional arguments
    # parser.add_argument("num1", help="Number1", type=float)
    # parser.add_argument("num2", help="Number2", type=float)
    # parser.add_argument("operation", help="provide operator",default="+")       # still it through error incase of change
                                                                                # parameters list in command line

    # optional arguments
    parser.add_argument('-a',"--num1", help="Number1", type=float)
    parser.add_argument('-b',"--num2", help="Number2", type=float)
    parser.add_argument('-c',"--operation", help="provide operator",default="-")


    # Parse the arguments
    args=parser.parse_args()
    print(args)
    result=None
    if args.operation=="+":
        result=args.num1+args.num2
    if args.operation=="-":
        result=args.num1-args.num2
    if args.operation=="*":
        result=args.num1*args.num2
    if args.operation=="pow":
        result=pow(args.num1,args.num2)

print("Result:",result)
