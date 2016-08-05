def getFeaturesForDrawing(envelope, columns):
    '''
    1, Loop all headers and get filtered headers by envelope
    3, get records by intersected header
    4, return filtered records
    '''
    recordsToDraw = getRecords(envelope)
    recordsToDraw = filterRecordsHandler?.invoke(recordsToDraw)
    
    
def getHeaders(envelope):
    yield header

def getRecords(envelope):
    drawingRecords = file.readRecordsInsideEnvelope(envelope)
    return drawingRecords

def readRecordsInsideEnvelope(self, envelope):
    header = self.readHeader()
    if header.length == 0: return None
    if header.envelope.disjoints(envelope): return None
    if(not filterRecordHandler?.invoke(header.envelope)): return None

    return self.readRecord()