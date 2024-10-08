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
      height: 100%;
      z-index: 1;
      /* object-fit: cover; */
    }}
    p{{
      width: 82%;
      position: absolute;
      top: 28%;
      left: 9%;
      padding: 10px;
      font-family: Calibri, sans-serif;
      font-size: 2vw;
    }}
    @media screen and (min-width:400px){{
      p{{
        top:31%;
        left:11%;
      }}
    }}

  </style>
  <body>
    <div class="container">
      <img src="/images/presi-1.png" alt="Letter">
      <p>
        Dear {fullName}, <br><br>

        <b>Congratulations</b> on your selection to the <b>Extended Executive Committee</b> for the 2024-25 term of the <b>NUCES KHI ACM Student Chapter!</b> We are excited to welcome you as the <b>{position}</b> of <b>Team {teamName}</b> and look forward to your leadership in driving the team’s success.<br><br>

        Your role will be pivotal in fulfilling the operational responsibilities expected from your team, and we believe your strategic insights and leadership will contribute greatly to our goals. With your expertise, we are confident that you will guide your team to deliver their best, ensuring that our objectives are met effectively.<br><br>

        We are committed to fostering a collaborative and supportive environment, and your leadership will play a crucial role in helping us grow as a cohesive unit.<br><br>

        Once again, congratulations and welcome to the team! We’re excited to see the impact we will make together.
        <br><br>

        Best Regards
      </p>
    </div>
  </body>
  </html>
  """