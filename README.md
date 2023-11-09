# IMAGE-SCALING-ON-THE-FLY-WITH-AMAZON-LAMBDA
Demonstration on outlining a method of lazily generating images, in which a resized asset is only created if a user requests that specific size.

# Introduction
With the explosion of device types used to access the Internet with different screen sizes, and resolutions, developers must often provide images in an array of sizes to ensure a great user experience. This can become complex to manage and drive up costs.
To overcome this, lets outline a method of lazily generating images, in which a resized asset is only created if a user requests that specific size.

# The Need for On-the-Fly Image Scaling
Instead of processing and resizing images into all necessary sizes upon upload, the approach of processing images on the fly has several upsides
Increased agility: When you redesign your website or application, you can add new dimensions on the fly, rather than working to reprocess the entire archive of images that you have stored.
Reduced storage costs: The approach of resizing on-demand means that developers do not need to store images that are not accessed by users.
Resilience to failure: If image processing is designed to occur only one time upon object creation, an intermittent failure in that process―or any data loss to the processed images―could cause continual failures to future users. When resizing images on-demand, each request initiates processing if a resized image is not found, meaning that future requests could recover from a previous failure automatically.

# Architecture overview
![image](https://github.com/rakshitasupadhya/IMAGE-SCALING-ON-THE-FLY-WITH-AMAZON-LAMBDA/assets/107621546/24d27446-c096-40d3-8f1b-82e5126deb5e)
1. Users will send a request to the API Gateway with the image size parameters(width/height) in order to receive the s3 URL of the resized image,
2. The API Gateway request will trigger a lambda function,
3. that will check if the image with the given size exists or not,
4. if it does this function will return the image s3 URL,
5. else it will take the original image from s3, resize it with the given size and return back the image s3 URL.

# Use Cases
1. Responsive Web Design: Automatically resize and serve images at different resolutions to match the viewer's device, ensuring optimal display on various screens, such as desktops, tablets, and mobile devices.
2. Thumbnail Generation: Create thumbnails for image galleries, product listings, or user-generated content. By resizing images on-the-fly, you save storage space and bandwidth.
3. User Profile Images: Allow users to upload high-resolution profile pictures, which are then resized to smaller dimensions for display in user profiles, comments, and avatars.
4. E-commerce: Automatically generate and serve product images in various sizes for category pages, product listings, and zoomed views.
5. Customized Image Downloads: Allow users to download images in specific sizes or formats for use in their own projects or publications.
6. Image Analytics: Capture analytics data on image access and usage, such as which sizes are most frequently requested or viewed.

# Implementation

1. Create S3 bucket by enabling ACl and making it public. Add Policy Generator
2. Upload Image to the bucket
3. Create Lambda function and deploy the code
4. Add Environment variables as mentioned in the document.
5. Increase the timeout limit to 1 min
6. Attach policies as mentioned in the document
7. Add layers to support Pillow function. ARN mentioned in the document.
8. Create HTTP API Gateway and link it with Lambda
9. Trigger the API endpoint via Postman by passing the parameters- size & image. (Refer the document for more details)







