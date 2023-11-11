import multiprocessing #import threading
import multiprocessing.queues as Queue 

    #creat prcoesses
    for i in range(0,NumberOfThreads-1):
        Thread_start_data=(lenSamples_x/NumberOfThreads)*i
        Thread_end_data=(lenSamples_x/NumberOfThreads)*(i+1)
        que = Queue.Queue()
        queue = np.append(queue,que)
        Thr=multiprocessing.Process(target=Process_main, args=(Samples_x[Thread_start_data:Thread_end_data+trainingSet[3]],Samples_y[Thread_start_data:Thread_end_data+trainingSet[3]],weights,dec_matrix,trainingSet[3],len(trainingSet[2]),queue[i]));
        thread = np.append(thread,Thr)
        thread[i].start()
		
	#wait for processes
    while True:
        ready=True
        for i in thread:
            if i.is_alive():
                ready=False
                
        if ready:
            break
        else:
            time.sleep(0.01)
			
    #get queued values from process
    posmatrix_X = []
    posmatrix_Y = []
    for i in range(0,(NumberOfThreads-1)):
        que_buffer = queue[i].get()
        posmatrix_X=np.append(posmatrix_X,que_buffer[0])
        posmatrix_Y=np.append(posmatrix_Y,que_buffer[1])
		
# process main functiuon
def Process_main(Samples_x,Samples_y, weights , dec_matrix,NoN,lenTrainSamples,q):
    pos_matrix=np.ones([2,len(Samples_x)-NoN])
    length_sam=len(Samples_x)-NoN
    Samples_x = copy.deepcopy(Samples_x)
    Samples_y = copy.deepcopy(Samples_y)
    for i in range(0,length_sam):
        # symbols x
        Sample_buffer = Samples_x[i:(i+NoN)] * weights
        
        Diff_allPts= np.abs(dec_matrix-np.matlib.repmat(Sample_buffer,lenTrainSamples,1))
        
        Diff_allPts=np.sum(Diff_allPts,axis=1)
        
        pos_matrix[0][i] = np.where(Diff_allPts == np.min(Diff_allPts))[0][0]
        
        #symbols y
        Sample_buffer = Samples_y[i:(i+NoN)] * weights
        
        Diff_allPts= np.abs(dec_matrix-np.matlib.repmat(Sample_buffer,lenTrainSamples,1))
        
        Diff_allPts=np.sum(Diff_allPts,axis=1)
        
        pos_matrix[1][i] = np.where(Diff_allPts == np.min(Diff_allPts))[0][0]
    
    q.put(pos_matrix)