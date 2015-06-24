# -*- coding: utf-8 -*-

import xml.parsers.expat
import mpcouch
import eventlet

currentTreeData = [] # just to initialize

def elementReader(filename):
    couchPusher = mpcouch.mpcouchPusher("http://localhost:5984/osmnodes",10000)
    def gotCompleteEntry(entry):
        couchPusher.pushData({'data':entry})
        pass
        #print(entry)
    
    def start_osm_element(name, attrs):
        global currentTreeData
        if   name == "node":
            '''start collecting information including all sub-keys'''
            currentTreeData = []
            currentTreeData.append(attrs) # the current meta-information
            currentTreeData.append({})    # for the tags
        elif name == "tag":
            '''collect the tag-information'''
            key = attrs[u'k']
            value = attrs[u'v']
            #print key
            #print value
            currentTreeData[1][key] = value
        else:
            print("uncatched element:")
            print(name)
    
    def end_osm_element(name):
        global currentTreeData
        if name == "node":
            '''the node has finished, store all information collected so far'''
            #lon = float(currentTreeData[0][u'lon'])
            #lat = float(currentTreeData[0][u'lat'])
            #idx.insert(int(currentTreeData[0][u'id']), (lon, lat, lon, lat), obj=currentTreeData)
            #print(currentTreeData)
            #gotCompleteEntry(currentTreeData)
            #e = eventlet.spawn(gotCompleteEntry,currentTreeData)
            e = eventlet.spawn(couchPusher.pushData,{'data':currentTreeData})
            e.wait()
            
    
    def char_osm_data(data):
        pass
    
    osmParser = xml.parsers.expat.ParserCreate()
    osmParser.StartElementHandler = start_osm_element
    osmParser.EndElementHandler = end_osm_element
    #osmParser.CharacterDataHandler = char_osm_data
    
    with open(filename, 'rb') as osmFile:
        print("start parsing")
        osmParser.ParseFile(osmFile)
        print("finished parsing")
    
    couchPusher.finish()

if __name__ == '__main__':
    print("running test")
    elementReader("/home/scubbx/Geodaten_lokal/austria.osh")
    print("finished test")
