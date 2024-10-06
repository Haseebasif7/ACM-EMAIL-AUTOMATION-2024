def getLetterWithAttributes(fullName,position,teamName):
  return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Automation</title>
</head>
<style>
  *{{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  .container{{
    position: relative;
    height: auto;

  }}
  .container img{{
    width: 100%;
    z-index: 1;
    /* object-fit: cover; */
  }}
  p{{
    width: 78%;
    position: absolute;
    top: 30%;
    left: 10%;
    padding: 10px;
    background-color: #ffffff80;
    box-shadow: 6px 6px 5px rgba(148, 138, 138, 0.9);
    font-family: Calibri, sans-serif;
  }}
  @media screen and (max-width:600px) {{
    p{{
      width: 80%;
      font-size: 2vw;
      white-space: wrap;
      box-shadow: 6px 6px 5px rgba(160, 155, 155, 0.9);
    }}
    .container{{
      white-space: wrap;
    }}
  }}
  @media screen and (min-width:600px) {{
    p{{
      width: 80%;
      font-size: 2vw;
      white-space: wrap;
    }}
  }}

</style>
<body>
  <div class="container">
    <img src="C:/Users/Asif/Desktop/acm/ACM-EMAIL-AUTOMATION-2024/images/pic.png" alt="">
    <!-- <div class="text-container"> -->
      <p>
        Dear {fullName}, <br><br>
  
        Welcome to the Extended Executive Committee of the ACM NUCES Karachi. We are excited to have you on board and look forward to the contributions you will make as {position} Team {teamName}.<br><br>
  
        It is worth acknowledging that the Extended ExCom of the ACM plays a crucial role in shaping the future of our event. Your involvement will be essential in crafting strategies, evaluating projects of your team members, and ensuring that our objectives align with the needs of our community. We believe in fostering a positive and collaborative work environment where everyone can grow and succeed together.<br><br>
  
        Our Extended ExCom is committed to creating a supportive and inclusive environment where everyone's voices are heard and respected. We are confident that your addition to our team will further enhance our cohesion and effectiveness.<br><br>
  
        Once again, welcome to the team! We are thrilled to have you with us and can't wait to see what we will achieve together.<br><br>
  
        Best Regards,<br>
      </p>
    <!-- </div> -->
  </div>
</body>
</html>
  """