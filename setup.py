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
        (os.path.join(usr_share, 'applications/'), ['electrum-xzc.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-xzc.png'])
    ]

setup(
    name="Electrum-XZC",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'scrypt>=0.6.0',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'PySocks>=1.6.6',
    ],
    packages=[
        'electrum_xzc',
        'electrum_xzc_gui',
        'electrum_xzc_gui.qt',
        'electrum_xzc_plugins',
        'electrum_xzc_plugins.audio_modem',
        'electrum_xzc_plugins.cosigner_pool',
        'electrum_xzc_plugins.email_requests',
        'electrum_xzc_plugins.hw_wallet',
        'electrum_xzc_plugins.keepkey',
        'electrum_xzc_plugins.labels',
        'electrum_xzc_plugins.ledger',
        'electrum_xzc_plugins.trezor',
        'electrum_xzc_plugins.digitalbitbox',
        'electrum_xzc_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_xzc': 'lib',
        'electrum_xzc_gui': 'gui',
        'electrum_xzc_plugins': 'plugins',
    },
    package_data={
        'electrum_xzc': [
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
    scripts=['electrum-xzc'],
    data_files=data_files,
    description="Lightweight Zcoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="http://electrum-xzc.org",
    long_description="""Lightweight Zcoin Wallet"""
)
