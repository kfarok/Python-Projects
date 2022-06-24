<html>
<head>
<title>badoo.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
badoo.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">selenium </span><span class="s0">import </span><span class="s1">webdriver</span>
<span class="s0">from </span><span class="s1">time </span><span class="s0">import </span><span class="s1">sleep</span>
<span class="s0">import </span><span class="s1">time</span>
<span class="s0">import </span><span class="s1">os</span>


<span class="s0">class </span><span class="s1">Bado(webdriver.Chrome):</span>
    <span class="s0">def </span><span class="s1">__init__(self</span><span class="s0">, </span><span class="s1">driver_path=</span><span class="s2">r&quot;/Users/kamyabfarokhi/Desktop/Chromedriver&quot;</span><span class="s1">):</span>
        <span class="s1">self.driver_path = driver_path</span>
        <span class="s1">os.environ[</span><span class="s2">'PATH'</span><span class="s1">] += driver_path</span>
        <span class="s1">self.implicitly_wait(</span><span class="s3">15</span><span class="s1">)</span>
        <span class="s1">self.maximize_window()</span>
        <span class="s1">super(Bado</span><span class="s0">, </span><span class="s1">self).__init__()</span>

    <span class="s0">def </span><span class="s1">login(self):</span>
        <span class="s1">self.get(</span><span class="s2">'https://badoo.com/signin/?f=top'</span><span class="s1">)</span>
        <span class="s1">sleep(</span><span class="s3">2</span><span class="s1">)</span>

        <span class="s1">username = self.find_element_by_xpath(</span><span class="s2">'/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div['</span>
                                                    <span class="s2">'1]/div[ '</span>
                                         <span class="s2">'2]/div/input'</span><span class="s1">)</span>
        <span class="s1">username.send_keys(USER)</span>
        <span class="s1">password = self.find_element_by_xpath(</span><span class="s2">'/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div['</span>
                                                    <span class="s2">'2]/div[ '</span>
                                         <span class="s2">'2]/div/input'</span><span class="s1">)</span>
        <span class="s1">password.send_keys(PASS)</span>

        <span class="s1">sign_button = self.find_element_by_xpath(</span>
            <span class="s2">'/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button'</span><span class="s1">)</span>
        <span class="s1">sign_button.click()</span>
        <span class="s1">sleep(</span><span class="s3">2</span><span class="s1">)</span>
        <span class="s1">self.fullscreen_window()</span>

    <span class="s0">def </span><span class="s1">like(self):</span>
        <span class="s1">self.find_element_by_xpath(</span><span class="s2">'/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]'</span><span class="s1">).click()</span>

    <span class="s0">def </span><span class="s1">dislike(self):</span>
        <span class="s1">self.find_element_by_xpath(</span><span class="s2">'/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div['</span>
                                         <span class="s2">'2]/div[2]/div[1]'</span><span class="s1">).click()</span>

    <span class="s0">def </span><span class="s1">unmatch(self):</span>
        <span class="s1">sleep(</span><span class="s3">5</span><span class="s1">)</span>
        <span class="s0">while True</span><span class="s1">:</span>
            <span class="s0">try</span><span class="s1">:</span>
                <span class="s1">message_btn = self.find_element_by_xpath(</span>
                    <span class="s2">'//*[@id=&quot;app_s&quot;]/div/div/div/div[1]/div/div[3]/div/a[3]'</span><span class="s1">)</span>
                <span class="s1">message_btn.click()</span>
                <span class="s1">print(</span><span class="s2">&quot;message check&quot;</span><span class="s1">)</span>
                <span class="s1">sleep(</span><span class="s3">1</span><span class="s1">)</span>
                <span class="s1">user = self.find_element_by_id(</span><span class="s2">'id=&quot;u_787511995&quot;&gt; == $0'</span><span class="s1">)</span>
                <span class="s1">user.click()</span>
                <span class="s1">print(</span><span class="s2">'user check'</span><span class="s1">)</span>
                <span class="s1">sleep(</span><span class="s3">1</span><span class="s1">)</span>
                <span class="s1">dots = self.find_element_by_xpath(</span><span class="s2">'//*[@id=&quot;im_wrapper&quot;]/header/div/div[1]/div[2]/div/div[1]'</span><span class="s1">)</span>
                <span class="s1">dots.click()</span>
                <span class="s1">print(</span><span class="s2">'dot checks'</span><span class="s1">)</span>
                <span class="s1">sleep(</span><span class="s3">1</span><span class="s1">)</span>
                <span class="s1">delete = self.find_element_by_xpath(</span><span class="s2">'/html/body/div[4]'</span><span class="s1">)</span>
                <span class="s1">delete.click()</span>
                <span class="s1">print(</span><span class="s2">&quot;delete check&quot;</span><span class="s1">)</span>
                <span class="s1">sleep(</span><span class="s3">2</span><span class="s1">)</span>
                <span class="s1">second_del = self.find_element_by_xpath(</span><span class="s2">'/html/body/aside/section/div['</span>
                                                              <span class="s2">'1]/div/form/div/section/div/div/div/div[1]'</span><span class="s1">)</span>
                <span class="s1">second_del.click()</span>
                <span class="s1">print(</span><span class="s2">'second check'</span><span class="s1">)</span>
                <span class="s1">sleep(</span><span class="s3">2</span><span class="s1">)</span>

            <span class="s0">except </span><span class="s1">Exception:</span>
                <span class="s1">self.close()</span>

    <span class="s0">def </span><span class="s1">auto_like(self):</span>
        <span class="s1">i = </span><span class="s3">1</span>
        <span class="s0">while </span><span class="s1">i &lt; </span><span class="s3">590</span><span class="s1">:</span>
            <span class="s1">i += </span><span class="s3">1</span>
            <span class="s1">sleep(</span><span class="s3">0.5</span><span class="s1">)</span>
            <span class="s0">try</span><span class="s1">:</span>
                <span class="s1">self.like()</span>
            <span class="s0">except </span><span class="s1">Exception:</span>
                <span class="s0">try</span><span class="s1">:</span>
                    <span class="s1">self.find_element_by_xpath(</span><span class="s2">'/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div'</span><span class="s1">).click()</span>
                <span class="s0">except</span><span class="s1">:</span>
                    <span class="s1">self.dislike()</span>
</pre>
</body>
</html>