<p align="center">
  <img width="350" src=https://github.com/softmatterlab/DeepTrack2/blob/develop/assets/logo.png?raw=true>
</p>

<h3 align="center">A comprehensive deep learning framework for digital microscopy.</h3>
<p align="center">
  <a href="/LICENSE" alt="licence"><img src="https://img.shields.io/github/license/softmatterlab/DeepTrack-2.0"></a>
  <a href="https://badge.fury.io/py/deeptrack"><img src="https://badge.fury.io/py/deeptrack.svg" alt="PyPI version"></a>
  <a href="https://softmatterlab.github.io/DeepTrack2/deeptrack.html"><img src="https://img.shields.io/badge/docs-passing-green" alt="PyPI version"></a>
  <a href="https://badge.fury.io/py/deeptrack"><img src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue" alt="Python version"></a>
  <a href="https://doi.org/10.1063/5.0034891" alt="DOI">
    <img src="https://img.shields.io/badge/DOI-10.1063%2F5.0034891-blue">
  </a>
</p>
<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#using-deeptrack">Examples</a> •
  <a href="#learning-deeptrack-21">Basics</a> •
  <a href="#cite-us">Cite us</a> •
  <a href="/LICENSE">License</a> 
</p>


We provide tools to create physical simulations of optical systems, to generate and train neural network models, and to analyze experimental data.

# Installation

DeepTrack 2.1 requires at least python 3.6.

To install DeepTrack 2.1, open a terminal or command prompt and run:

    pip install deeptrack
    
If you have a very recent version of python, you may need to install numpy _before_ DeepTrack. This is a known issue with scikit-image.

### Updating to 2.1 from 2.0

If you are already using DeepTrack 2.0 (pypi version 0.x.x), updating to DeepTrack 2.1 (pypi version 1.x.x) is painless. If you have followed deprecation warnings, no change to your code is needed. There are two breaking changes:

- The deprecated operator `+` to chain features has been removed. It is now only possible using the `>>` operator.
- The deprecated operator `**` to duplicate a feature has been removed. It is now only possible using the `^` operator.

If you notice any other changes in behavior, please report it to us in the issues tab.

# Examples of applications using DeepTrack 

DeepTrack is a general purpose deep learning framework for microscopy, meaning you can use it for any task you like. Here, we show some common applications!

<br/>
<h3 align="left"> Single particle tracking </h3>
<p align="left">
  <img width="300" src=/assets/SPT-ideal.gif?raw=true>
  <img width="300" src=/assets/SPT-noisy.gif?raw=true>
  <br/>
  <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/paper-examples/2-single_particle_tracking.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Training a CNN-based single particle tracker using simulated data </a>
  <br/>
  <a href="https://doi.org/10.1038/s41467-022-35004-y" alt="DOI lodestar">
    <img src="https://img.shields.io/badge/DOI-10.1038%2Fs41467--022--35004--y-blue">
  </a> 
  <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/LodeSTAR/02.%20tracking_particles_of_various_shapes.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Unsupervised training of a single particle tracker using LodeSTAR </a> 
  
</p>
<br/>

<h3 align="left"> Multi-particle tracking </h3>

<p align="left">
  <img width="600" src=/assets/MPT-packed.gif?raw=true>
  <br/>
  <a href="https://doi.org/10.1038/s41467-022-35004-y" alt="DOI lodestar">
    <img src="https://img.shields.io/badge/DOI-10.1038%2Fs41467--022--35004--y-blue">
  </a> <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/LodeSTAR/03.track_BF-C2DL-HSC.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Training LodeSTAR to detect multiple cells from a single image </a>
  <br/>
  <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/paper-examples/4-multi-molecule-tracking.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Training a UNet-based multi-particle tracker using simulated data </a> 
</p>
<br/>

<h3 align="left"> Particle tracing </h3>

<p align="left">
  <img width="600" src=/assets/Tracing.gif?raw=true>
  <br/>
  <a href="https://doi.org/10.48550/arXiv.2202.06355" alt="DOI magik">
    <img src="https://img.shields.io/badge/DOI-10.48550%2FarXiv.2202.0635-blue">
  </a>  <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/develop/examples/MAGIK/cell_migration_analysis.ipynb"> <img     src="https://colab.research.google.com/assets/colab-badge.svg"> Training MAGIK to trace migrating cells </a>
</p>

# Basics to learn DeepTrack 2.1

Everybody learns in different ways! Depending on your preferences, and what you want to do with DeepTrack, you may want to check out one or more of these resources.

## Getting-started guides

We have two separate series of notebooks which aims to teach you all you need to know to use DeepTrack to its fullest. The first is a set of six notebooks with a focus on the application.

1. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/get-started/01.%20deeptrack_introduction_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> deeptrack_introduction_tutorial </a>  gives an overview of how to use DeepTrack 2.1.
2. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/tutorials/tracking_particle_cnn_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> tracking_particle_cnn_tutorial </a> demonstrates how to track a point particle with a convolutional neural network (CNN).
3. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/tutorial/tracking_multiple_particles_unet_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> tracking_particle_cnn_tutorial </a> demonstrates how to track multiple particles using a U-net.
4. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/tutorials/characterizing_aberrations_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> characterizing_aberrations_tutorial </a> demonstrates how to add and characterize aberrations of an optical device. 
5. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/tutorials/distinguishing_particles_in_brightfield_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> distinguishing_particles_in_brightfield_tutorial </a> demonstrates how to use a U-net to track and distinguish particles of different sizes in brightfield microscopy. 
6. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/tutorials/analyzing_video_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> analyzing_video_tutorial </a> demonstrates how to create videos and how to train a neural network to analyze them.


The second series focuses on individual topics, introducing them in a natural order. 

1. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/get-started/01.%20deeptrack_introduction_tutorial.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Introducing how to create simulation pipelines and train models. </a>
2. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/get-started/02.%20using_deeptrack_generators.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Demonstrating data generators. </a> 
3. <a href="https://colab.research.google.com/github/softmatterlab/DeepTrack-2.0/blob/master/examples/get-started/03.%20customizing_deeptrack_models.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg"> Demonstrating how to customize models using layer-blocks. </a> 

## DeepTrack 2.1 in action

Additionally, we have seven more case studies which are less documented, but gives additional insight in how to use DeepTrack with real datasets

1. [MNIST](examples/paper-examples/1-MNIST.ipynb) classifies handwritted digits.
2. [single particle tracking](examples/paper-examples/2-single_particle_tracking.ipynb) tracks experimentally captured videos of a single particle. (Requires opencv-python compiled with ffmpeg to open and read a video.)
3. [single particle sizing](examples/paper-examples/3-particle_sizing.ipynb) extracts the radius and refractive index of particles.
4. [multi-particle tracking](examples/paper-examples/4-multi-molecule-tracking.ipynb) detects quantum dots in a low SNR image.
5. [3-dimensional tracking](examples/paper-examples/5-inline_holography_3d_tracking.ipynb) tracks particles in three dimensions.
6. [cell counting](examples/paper-examples/6-cell_counting.ipynb) counts the number of cells in fluorescence images.
7. [GAN image generation](examples/paper-examples/7-GAN_image_generation.ipynb) uses a GAN to create cell image from masks.

## Model-specific examples

We also have examples that are specific for certain models. This includes 
- [*LodeSTAR*](examples/LodeSTAR) for label-free particle tracking.
- [*MAGIK*](deeptrack/models/gnns/) for graph-based particle linking and trace characterization.

## Documentation
The detailed documentation of DeepTrack 2.1 is available at the following link: https://softmatterlab.github.io/DeepTrack2/deeptrack.html

## Video Tutorials

Videos are currently being updated to match with the current version of DeepTrack.

## Cite us!
If you use DeepTrack 2.1 in your project, please cite us here:

```
Benjamin Midtvedt, Saga Helgadottir, Aykut Argun, Jesús Pineda, Daniel Midtvedt, Giovanni Volpe.
"Quantitative Digital Microscopy with Deep Learning."
Applied Physics Reviews 8 (2021), 011310.
https://doi.org/10.1063/5.0034891
```

See also:

<https://www.nature.com/articles/s41467-022-35004-y>:
```
Midtvedt, B., Pineda, J., Skärberg, F. et al. 
"Single-shot self-supervised object detection in microscopy." 
Nat Commun 13, 7492 (2022).
```

<https://arxiv.org/abs/2202.06355>:
```
Jesús Pineda, Benjamin Midtvedt, Harshith Bachimanchi, Sergio Noé, Daniel  Midtvedt, Giovanni Volpe,1 and  Carlo  Manzo
"Geometric deep learning reveals the spatiotemporal fingerprint ofmicroscopic motion."
arXiv 2202.06355 (2022).
```

<https://doi.org/10.1364/OPTICA.6.000506>:
```
Saga Helgadottir, Aykut Argun, and Giovanni Volpe.
"Digital video microscopy enhanced by deep learning."
Optica 6.4 (2019): 506-513.
```

<https://github.com/softmatterlab/DeepTrack.git>:
```
Saga Helgadottir, Aykut Argun, and Giovanni Volpe.
"DeepTrack." (2019)
```

## Funding

This work was supported by the ERC Starting Grant ComplexSwimmers (Grant No. 677511), the ERC Starting Grant MAPEI (101001267), and the Knut and Alice Wallenberg Foundation.
