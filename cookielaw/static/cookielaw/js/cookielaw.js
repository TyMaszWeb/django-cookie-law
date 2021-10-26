var Cookielaw = {
    ACCEPTED: '1',
    REJECTED: '0',

    createCookie: function (name, value, days, secure=true) {
        var date = new Date(),
            expires = '';
        if (days) {
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        
        var secureString = "";
        if (window.isSecureContext && secure) {
            secureString = "; Secure";
        }
        
        document.cookie = name + "=" + value + expires + "; path=/" + secureString;
    },

    createCookielawCookie: function (cookieValue, secure=true) {
        cookieValue = cookieValue || this.ACCEPTED;
        this.createCookie('cookielaw_accepted', cookieValue, 10 * 365, secure);

        if (typeof (window.jQuery) === 'function') {
            jQuery('#CookielawBanner').slideUp();
        } else {
            document.getElementById('CookielawBanner').style.display = 'none';
        }
    },

    accept: function () {
        this.createCookielawCookie(this.ACCEPTED);
    },

    reject: function () {
          this.createCookielawCookie(this.REJECTED);
    }
};
