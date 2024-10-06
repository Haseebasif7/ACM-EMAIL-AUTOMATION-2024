def getLetterWithAttributes(fullName, position, teamName):
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
  }}
  p{{
    width: 78%;
    position: absolute;
    top: 30%; /* Adjusted this value to move text higher by two lines */
    left: 10%;
    padding: 10px;
    background-color: #ffffff80;
    font-family: Calibri, sans-serif;
    font-size: 1.4em; /* Slightly reduced font size */
    margin-top: 20px; /* Reduced space above the text */
  }}
  @media screen and (max-width:600px) {{
    p{{
      width: 80%;
      font-size: 2.8vw; /* Adjusted for smaller screens */
      white-space: wrap;

    }}
    .container{{
      white-space: wrap;
    }}
  }}
  @media screen and (min-width:600px) {{
    p{{
      width: 80%;
      font-size: 2.3vw; /* Adjusted for larger screens */
      white-space: wrap;
    }}
  }}
</style>
<body>
  <div class="container">
    <img src="C:/Users/Asif/Desktop/acm/pic.png" alt="">
    <p>
      Dear {fullName}, <br><br>

      Welcome to the Extended Executive Committee of the ACM NUCES Karachi. We are excited to have you on board and look forward to the contributions you will make as {position} Team {teamName}.<br><br>

      It is worth acknowledging that the Extended ExCom of the ACM plays a crucial role in shaping the future of our event. Your involvement will be essential in crafting strategies, evaluating projects of your team members, and ensuring that our objectives align with the needs of our community. We believe in fostering a positive and collaborative work environment where everyone can grow and succeed together.<br><br>

      Our Extended ExCom is committed to creating a supportive and inclusive environment where everyone's voices are heard and respected. We are confident that your addition to our team will further enhance our cohesion and effectiveness.<br><br>

      Once again, welcome to the team! We are thrilled to have you with us and can't wait to see what we will achieve together.<br><br>

      Best Regards,<br>
    </p>
  </div>
</body>
</html>
    """

