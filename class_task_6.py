class Foo:
    def __init__(self, infile, outfile):

    def __enter__(self, infile, outfile):
        self.fr = open(self.infile, 'r')
        self.line = self.fr.read(1)
        self.wr = open(self.outfile)
        self.wr.write(self.line)

    def __exit__(self, *args):



