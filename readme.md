
## About

I have built an image annotation application using :
- FastAPI : Backend
- Angular: Frontend
- Pinata : Blob/File Storage

This application would help in doing the annotations of the image dataset. Then these annotations could be exported and be used for AI model training.

## Demo
<!-- Share a link to your application and include some screenshots here. -->

 <!-- [![https://www.youtube.com/embed/ZICO88vXu6Y?si=IlZYirZS42934Y0r](https://www.youtube.com/embed/ZICO88vXu6Y?si=IlZYirZS42934Y0r)]() -->
**Youtube Demo Video**

[![Youtube Demo Video](https://img.youtube.com/vi/ZICO88vXu6Y/0.jpg)](https://www.youtube.com/watch?v=ZICO88vXu6Y)
<!-- 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wyf8ltwo2ur4hxwd6c50.png) -->


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bbcsvzi72woaoi2fthav.png)

## My Code
<!-- Share a link to your code (Tip: you can embed GitHub projects directly into this post). -->

- backend Fastapi : https://github.com/suyash-srivastava-dev/annotation-editor-backend
- frontend Angular : https://github.com/suyash-srivastava-dev/annotation-editor


## Flow Diagram


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4phtzti3a9a8o4441s4p.png)



## Pinata setup
- Create an account with Pinata, and fetch the keys.
- Install and setup .env files
```sh
npm i pinata
```

```js
PINATA_API_KEY=""
PINATA_API_SECRET=""
PINATA_GATEWAY="*.mypinata.cloud"
PINATA_JWT=""
```

```js
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});

```
- Create methods for Upload & Retrieve Files

Upload File
```js
const file = new File(["hello"], "Testing.txt", { type: "text/plain" });
    const upload = await pinata.upload.file(file);
    console.log(upload);
```
Retrieve Files
```js
const url = await pinata.gateways.createSignedURL({
       	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
    	expires: 1800,
    })
    console.log(url)
```



## More Details
<!-- Share clear examples of how you used Pinata. -->

Pinata group was created for each project in the application.
Pinata was used for saving the image dataset, with & without annotations. Also the annotation files are saved as JSON on Pinata. Access to the images & Json file is through the signed SDK.

<!-- Team Submissions: Please pick one member to publish the submission and credit teammates by listing their DEV usernames directly in the body of the post. -->

<!-- Don't forget to add a cover image (if you want). -->

<!-- Thanks for participating! -->