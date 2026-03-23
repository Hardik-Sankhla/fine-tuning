"""Starter training script placeholder"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='../configs/train.yaml')
    args = parser.parse_args()
    print('Run training with config:', args.config)


if __name__ == '__main__':
    main()
