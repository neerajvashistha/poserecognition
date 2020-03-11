## Pose Recognition
A samll work to demonstrate pose recoginition using openpose


## Openpose Installation
Clone the master branch of open pose
```
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
```

Uninstall cmake and reinstall from source
```
sudo apt purge cmake-qt-gui
sudo apt-get install qtbase5-dev libssl-dev
```

```
tar xvzf Downloads/cmake-3.17.0-rc2.tar.gz
cd cmake-3.17.0-rc2.tar.gz
./configure --qt-gui
./bootstrap && make -j`nproc` && sudo make install -j`nproc`
```

Follow the guidelines mentioned at my [medium](https://medium.com/@neerajvash8/getting-your-hand-dirty-on-ubuntu-18-04-tensorflow-1-13-1-cuda10-0-f7a49f42a22f) to install Cuda 10 Cudnn 7.5 tensorflow 1.13.1


Install open-cv and hdf5

```
sudo apt-get --assume-yes install libatlas-base-dev libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get --assume-yes install --no-install-recommends libboost-all-dev
```

```
sudo apt-get --assume-yes install libopencv-dev
sudo apt-get --assume-yes install opencl-headers ocl-icd-opencl-dev libviennacl-dev
```

Install nympy protobuf and opencv using pip for python

```
sudo -H pip3 install --upgrade numpy protobuf opencv-python
```

Caffe installation requirements

```
sudo apt-get install libopenblas-dev
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```

Caffe installation

```
git clone https://github.com/BVLC/caffe.git
```

Switch to a different branch as there is layering issue in current version discussed [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/787)

```
git checkout f019d0dfe86f49d1140961f8c7dec22130c8315 
```

Edit `Makefile.config` according to this [page](https://mc.ai/installing-caffe-on-ubuntu-18-04-with-cuda-and-cudnn/)

Install Caffe
```
make all -j4 # 4 represents number of CPU Cores
make pycaffe -j4 # 4 represents number of CPU Cores
export PYTHONPATH=~/caffe/python:$PYTHONPATH
export Caffe_INCLUDE_DIRS=/home/nv/caffe/include/caffe
export Caffe_LIBS=/home/nv/caffe/.build_release/lib/
```

Pybind11 installation

```
git clone https://github.com/pybind/pybind11.git
cd pybind11
mkdir -p build
cd build
cmake .. -DDOWNLOAD_CATCH=1
make check -j 4
export PYBIND=/usr/local/share/cmake/pybind11
```

Follow steps to configure openpose as described [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md#openpose-configuration )

Finally install Openpose
```
cd build/
make -j`nproc`
```

## Running the project
After making sure openpose is installed and working as described [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/quick_start.md#running-on-video), either place the file `pose_reco.py` at `openpose/build/examples/tutorial_api_python` or follow the guideline [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/modules/python_module.md#exporting-python-openpose) to run the file outside the example directory.

To run the project on terminal, execute
```
python pose_reco.py --video ~/openpose/examples/media/video.avi
```

The output would be a Body keypoints, identified in the video buffer.

## Common Issues
It may happen that you may run out of memory, and core dump is seen
such as 
```
Auto-detecting all available GPUs... Detected 1 GPU(s), using 1 of them starting at GPU 0.
F0310 22:17:02.648015 12379 syncedmem.cpp:71] Check failed: error == cudaSuccess (2 vs. 0)  out of memory
*** Check failure stack trace: ***
    @     0x7f820393a0cd  google::LogMessage::Fail()
    @     0x7f820393bf33  google::LogMessage::SendToLog()
    @     0x7f8203939c28  google::LogMessage::Flush()
    @     0x7f820393c999  google::LogMessageFatal::~LogMessageFatal()
    @     0x7f820352a19a  caffe::SyncedMemory::mutable_gpu_data()
    @     0x7f820351f4f2  caffe::Blob<>::mutable_gpu_data()
    @     0x7f8203534afc  caffe::PReLULayer<>::Forward_gpu()
    @     0x7f82034b7442  caffe::Net<>::ForwardFromTo()
    @     0x7f8203f9b5e3  op::NetCaffe::forwardPass()

```

For such issues, we need to run caliberation described [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/modules/calibration_module.md)

