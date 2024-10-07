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
    top: 220px; /*Adjusted this value to move text higher by two lines*/
    left: 62px;
    padding: 10px;
    background-color: #ffffff00;
    font-family: Calibri, sans-serif;
    font-size: 0.65em; /* Slightly reduced font size */
    margin-top: 20px; /* Reduced space above the text */
  }}
  
</style>
<body>
  <div class="container">
    <img src="assets/letter_template.jpg" alt="">
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

