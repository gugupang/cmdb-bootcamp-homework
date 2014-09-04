import sys

class FASTAReader(object):
    def __init__( self, file ):
        self.file = file
        self.last_sid = None
    def next( self ):
        if self.last_sid is None:
            line = sys.stdin.readline()
            assert line.startswith(">")
            sid = line[1:].rstrip("\r\n")
        else:
            sid = self.last_sid
        
        sequences = []
        while True:
            line = sys.stdin.readline()
            if line == "" and not sequences:
                raise StopIteration 
            if line.startswith(">") or line == "":
                self.last_sid = line[1:].rstrip("\r\n")
                break
            else:
                sequences.append (line.strip())
        
        sequence = "".join( sequences )
        return sid, sequence
    def __iter__( self ):
        return self