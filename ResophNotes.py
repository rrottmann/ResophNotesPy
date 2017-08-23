#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ResophNotes.py

Convert to JSON and query ResophNotes notes from shell.

Copyright 2017 by Reiner Rottmann <reiner@rottmann.it
Released under the BSD License.
"""
import os
import sys
import base64
import uuid
import json
import argparse
import subprocess
import collections
import xmltodict


def convert(path):
    """Convert the ResophNotes data file (resophnotesdata.xml) at given path. Returns db as dict."""
    tags = {}
    db = {}
    fd = open(path, 'r')
    content = fd.read()
    fd.close()
    data = xmltodict.parse(content)
    tags['none'] = []
    for tag in data['database']['tag']:
        try:
            tags[base64.b64decode(str(tag))] = []
        except KeyError:
            print tag
    for obj in data['database']['object']:
        uid = str(uuid.uuid4())
        try:
            if 'tags' in obj:
                objtags = base64.b64decode(str(obj['tags'])).split(',')
            else:
                objtags = ['none']
            for tag in objtags:
                tags[tag].append(uid)
                db[uid] = {}
                for key in obj.keys():
                    if key in ['content', 'tags']:
                        value = base64.b64decode(str(obj[key]))
                    else:
                        value = str(obj[key])
                    db[uid][key] = value
        except:
            pass
    return db


def save_json(path, db):
    """Save the db as JSON dump to given path."""
    fd = open(path, 'w')
    json.dump(db, fd)
    fd.close()


def open_json(path):
    """Open the db from JSON file previously saved at given path."""
    fd = open(path, 'r')
    return json.load(fd)


def count_tags(db):
    """Count tag statistics for some awesomeness."""
    all_tags = []
    for key in db.keys():
        obj = db[key]
        if 'tags' in obj.keys():
            all_tags = all_tags + obj['tags'].split(',')
    stats = collections.Counter(all_tags)
    return stats.most_common(10)


def cli(db, internal=False):
    """Query the database via CLI. May use internal viewer instead of less."""
    count_tags(db)
    print """
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|R|e|s|o|p|h|N|o|t|e|s|.|p|y|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """
    print 'Total number of notes:', len(db)
    print 'Most common tags:', ', '.join(['@' + x[0] + ':' + str(x[1]) for x in count_tags(db)])
    print ''
    while True:
        query = raw_input('Query (q to quit)? ').lower()
        if query == 'q':
            sys.exit(0)
        results = []
        for key in db.keys():
            obj = db[key]
            match_tag = True
            for q in query.split():
                if 'tags' in obj.keys():
                    if not q in str(obj['tags']).lower().split(','):
                        match_tag = False
                        break
                else:
                    match_tag = False
                    break
            if match_tag:
                if not obj in results:
                    results.append(obj)
                    continue
            if 'content' in obj.keys():
                if obj['content'].encode('utf-8').lower().find(query) > 0:
                    if not obj in results:
                        results.append(obj)
                        continue
        i = 0
        for result in results[:36]:
            if not 'tags' in result.keys():
                result['tags'] = 'none'
            print str(i), '|', result['modify'], '|', result['content'].splitlines()[0], '|', 'tags:', ' '.join(
                ['@' + x for x in result['tags'].split(',')])
            i += 1
        print 'Results:', len(results)
        if len(results) > 0:
            while True:
                show = str(raw_input('Read which note (q to return)? '))
                if show == 'q':
                    break
                if show.isdigit():
                    show = int(show)
                    if show >= 0 and show <= len(results):
                        if internal:
                            sys.stdout.write(str(results[show]['content']))
                        else:
                            p = subprocess.Popen('/usr/bin/less', stdin=subprocess.PIPE, shell=True)
                            p.communicate(results[show]['content'].encode('utf-8').strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert to JSON and query ResophNotes notes from shell.')
    parser.add_argument('--data', help='Import from this ResophNotes data file. Default: resophnotesdata.xml',
                        default='resophnotesdata.xml')
    parser.add_argument('--json', help='JSON file with converted ResophNotes data. Default: resophnotesdata.json',
                        default='resophnotesdata.json')
    parser.add_argument('--cli', help='Open an interactive cli to query ResophNotes data.', action='store_true')
    parser.add_argument('--internal', help='Use internal viewer instead of less.', action='store_true')
    args = parser.parse_args()
    db = None
    if not os.path.exists(args.json) and os.path.exists(args.data):
        db = convert(args.data)
        save_json(args.json, db)
    else:
        if os.path.exists(args.json):
            db = open_json(args.json)
    if db is None and os.path.exists(args.json):
        db = open_json(args.json)
    else:
        if db:
            if args.cli:
                cli(db, args.internal)
                sys.exit(0)
        else:
            print "Error: No ResophNotes available."
            sys.exit(1)
    parser.print_help()
    sys.exit(0)
