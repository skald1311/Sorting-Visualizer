

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/skald1311/Sorting-Visualizer">
    <img src="https://assets-global.website-files.com/606a802fcaa89bc357508cad/6123c034286044167618b263_7.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Sorting Visualizer</h3>

  <p align="center">
    A program that helps to visualize the five sorting algorithms
    <br />
    <a href="https://github.com/skald1311/Sorting-Visualizer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/skald1311/Sorting-Visualizer/issues">Report Bug</a>
    ·
    <a href="https://github.com/skald1311/Sorting-Visualizer/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a sorting visualizer program implemented with Pygame in Python is an interactive tool that visually demonstrates how five particular sorting algorithms work (includes Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort). These five specific sorting algorithms are those that I have learned in CMPUT 175 and as it is often difficult to illustrate these by words, I have decided to make a visualizer of my own to help others understand. I not only get an opportunity to reinforce and enhance my understanding of the material but also provide instructors with a tool that can assist their students in visualizing the algorithms. This program not only allows users to select a sorting algorithm of their choice, but also allows users to change the speed of the sorting. One convenient aspect of the sorting speed is that users have the ability to modify it **during the sorting process**. This means that if the user begins with a high speed, they can switch it to a lower speed if they desire, and vice versa.

Here's a picture of the interface: ![image](https://user-images.githubusercontent.com/84189062/230749957-c80f5875-6efa-4b97-855e-fe5c60e30f99.png)

<pre>
Controls: R - Reset and give a new random array
          SPACE - Start Sorting with chosen sorting algorithm
          J - Slow speed - tick(20)
          K - Fast speed - tick(60)
          A - Bubble Sort
          S - Selection Sort
          D - Insertion Sort
          F - Merge Sort
          G - Quick Sort
</pre>

If you press SPACE, the program then animates the sorting process with the current chosen sorting algorithm, displaying the current state of the array at each step, providing a clear visual representation of how the sorting algorithm is rearranging the elements of the array. I have included several demo videos of different sorting algorithms in the video folder. If you are unable or unwilling to download the visualizer, you may still view the videos to gain an understanding of how the algorithms work. I also included a super slow video on the Quick Sort as I didn't know how to make the visualization of the Quick Sort slower. Merge Sort is the same but I didn't include a video for that.

A frame of the sorting process:
![image](https://user-images.githubusercontent.com/84189062/230750407-6e9c4955-dc10-4f5d-afb7-cb33360ff7ec.png)


If you are curious about the reasons behind my usage of pygame or my overall development approach, you may refer to my journal.txt. This journal documents my progression throughout the project, including my reasoning and failed attempts.







<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Click the green button

![image](https://user-images.githubusercontent.com/84189062/210023644-49f6ee47-b8aa-479d-b192-c9985ef913cd.png)
   
   
2. Download ZIP

   ![image](https://user-images.githubusercontent.com/84189062/210023664-4d06ef4a-71a7-444d-9778-bf21c8ed30ae.png)
  
  
3. Extract the file
   ```sh
   Make sure all of the files are in the same folder!!!
   ```
4. Open up cmd (by searching cmd in the search bar)

![image](https://user-images.githubusercontent.com/84189062/230750573-78d12ddd-ba80-4235-b63f-cbfe66fecacf.png)

5. Type in cmd
   ```sh
   pip install pygame
   ```
   If this doesn't work, try finding your OS installation instructions here: https://www.pygame.org/wiki/GettingStarted
   
6. Run main.py in the extracted folder

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Duong Hoang - [LinkedIn](https://www.linkedin.com/in/hmd1311/)

Project Link: [https://github.com/skald1311/Sorting-Visualizer](https://github.com/skald1311/Sorting-Visualizer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hmd1311/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org

