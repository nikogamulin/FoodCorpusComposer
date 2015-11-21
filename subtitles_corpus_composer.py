import os, shutil, re, files
import glob

CORPUS_FILE = './data/corpus.txt'

def converttotxt():
    """
    Compose a corpus file for later usage in transcript_corpus_word2vec
    """
    destfolder = "./data/cleaned_txt"
    sourceFolder = "./data/subtitles"
    if not os.path.exists(destfolder):
        os.mkdir(destfolder)
    filenames = glob.glob(sourceFolder + "/*.srt")
    for subtitlesFile in filenames:
        destFileRoot = subtitlesFile.replace(sourceFolder, "")[0:-4]
        dest = "%s%s.txt" % (destfolder, destFileRoot)
        content = cleanup(subtitlesFile, dest, purgenewlines = True, lowercase = True)
        with open(CORPUS_FILE,'a+') as f: f.write(content)
    return

def cleanup(src, dest, purgenewlines = True, lowercase = True):
    """
    remove extraneous characters/information from the subtitle files
    this got REALLY slow at one point and I'm not sure why, but it can be fixed by commenting stuff out of the loop
    """
    timestamp = re.compile('^\d+\n?.*\n?', re.MULTILINE)
        #finds line numbers and the line after them (which usually houses timestamps)
    brackets = re.compile('\[[^]]*\]\n?|\([^)]*\)\n?|<[^>]*>\n?|\{[^}]*\}\n?')
        #finds brackets and anything in between them (sound effects)
    opensubs = re.compile('.*subtitles.*\n?|.*subs.*\n?', re.IGNORECASE)
        #finds the opensubtitles signature
    urls = re.compile('www.*\s\n?|[^\s]*\. ?com\n?')
        #finds any urls
    r = re.compile('\r')
        #gets rid of \r
    punctuation = re.compile("[^\w\s']")
        #finds punctuation
    n = re.compile('\n')
        #finds newlines
    print "fetching", src
    with open(src, 'r') as f:
        content = f.read()
        print "cleaning up", src
        content = timestamp.sub('', content)
        content = brackets.sub('', content)
        content = opensubs.sub('', content)
        content = urls.sub('', content)
        content = r.sub('', content)
        #content = punctuation.sub(' ', content)
        if purgenewlines:
            content = n.sub(' ', content)
        if lowercase:
            content = content.lower()
        return content

def getCorpus(existing=False):
    if not existing:
        #delete existing corpus file and create a new one
        try:
            os.remove(CORPUS_FILE)
        except:
            print "The corpus file doesn't exist"
        converttotxt()

    f= open(CORPUS_FILE, 'r')
    corpus = f.read()
    return corpus


if __name__ == "__main__":
    converttotxt()