#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 4, 0):
    sys.exit("Error: Electrum requires Python version >= 3.4.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-actinium.desktop']),
        (os.path.join(usr_share, 'icons/'), ['icons/electrum-actinium.png'])
    ]

setup(
    name="Electrum-Actinium",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'PySocks>=1.6.6',
    ],
    packages=[
        'electrum_acm',
        'electrum_acm_gui',
        'electrum_acm_gui.qt',
        'electrum_acm_plugins',
        'electrum_acm_plugins.audio_modem',
        'electrum_acm_plugins.cosigner_pool',
        'electrum_acm_plugins.email_requests',
        'electrum_acm_plugins.hw_wallet',
        'electrum_acm_plugins.labels',
        'electrum_acm_plugins.ledger',
        'electrum_acm_plugins.trezor',
        'electrum_acm_plugins.digitalbitbox',
        'electrum_acm_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_acm': 'lib',
        'electrum_acm_gui': 'gui',
        'electrum_acm_plugins': 'plugins',
    },
    package_data={
        'electrum_acm': [
            'servers.json',
            'servers_testnet.json',
            'currencies.json',
            'checkpoints.json',
            'checkpoints_testnet.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-actinium'],
    data_files=data_files,
    description="Lightweight Actinium Wallet",
    author="The Actinium Project",
    author_email="info@actinium.org",
    license="MIT Licence",
    url="https://actinium.org",
    long_description="""Lightweight Actinium Wallet"""
)
