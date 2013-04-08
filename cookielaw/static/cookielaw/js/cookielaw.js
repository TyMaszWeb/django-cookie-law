var Cookielaw = {

    createCookie: function (name, value, days) {
        if (days) {
            var date = new Date();
            date.setTime(date.getTime()+(days*24*60*60*1000));
            var expires = "; expires="+date.toGMTString();
        }
        else var expires = "";
        document.cookie = name + "=" + value + expires + "; path=/";
    },

    createCookielawCookie: function () {
        this.createCookie('cookielaw_accepted', '1', 10*365);

        if (typeof(window.jQuery) === 'function') {
            jQuery('#CookielawBanner').slideUp();
        } else {
            document.getElementById('CookielawBanner').style.display = 'none';
        }
    }

}
