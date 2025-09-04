#!/usr/bin/env python3

import gradio as gr 

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--server_port', default=8888, type=int)
parser.add_argument('--server_name', default=None, type=str)
parser.add_argument('--root_path', default=None, type=str) 

args = parser.parse_args()

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

iface.launch(server_port=args.server_port, 
					 server_name=args.server_name, 
					 root_path=args.root_path)
