from tkinter.ttk import Style
from tkinter import PhotoImage


class StylesInterface(Style):

    ServiceGroupStyleImage = PhotoImage
    ServiceGroupStyleImageFocus = PhotoImage
    ButtonStyleImage = PhotoImage

    def __init__(self, master=None):
        super().__init__(master=master)

        self.ServiceGroupStyleImage = PhotoImage("frameBorder", data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAALKSURBVHhe7Zs7bxNBFIXvjNfGduzEtojiKEQIaGiAngYKkMK/MAV1qOA3QAO0UPAvSEMBFXWgoQAhBVm2ATl2/Ey8D+bM3lg2khEFRbx3Pik60u4o0jk7r8JH1Wq1OhEVzd8ckUrTqHCdhivX6OTcRfK9VU2U8vj1GSfwPb8bZo4PKD/4RLn+R1LRhN/N0UMAR0qpmQAU9VdvUqdyj8JUnnLDz5QZfyPPPzT/xOcxZ5tIeeaDlek4e4nG+aukgyGV2m+ocPQBb+NBhiiK5gMIdZ5+Ve/TOHeZ1g7fUrHzjnQ4soOXlVDnqFe6Td3yHcqOvtL55uupJwRgpnUMzDcv7NrkNg+e0Fp7b+nNA3iAl83vT423CrW2dm0op3AAyn55s8apWn9G6cmP+HGCSJ+0jLfndnnEXpV9bgPAmse0X2+8NOtlYF8kER30ab35yni9Yj3bZ9jtseFhzSfxy/8JZgK8dio7djZoHHXY7bHhSaHYeW88r5hj/gZpnPM46pKw4f0rOhxaz/CuccnBOS8NeIZ3jRseLjnSgGd4t9fbZbnh/U9izylvehGSiguAVSwuAFaxuABYxeICYBWLC4BVLC4AVrG4AFjF4gJgFYsLgFUsLgBWsbgAWMXiAmAViwuAVSwuAFaxuABYxeICYBWLC4BVLC4AVrG4AFjF4gJgFYsJIPDxs3FpxJ4DX6NdhZqMNOAZ3jWqZWhXSQOe4V2jV4dq2WyRKOmgIAbP8K5RKkSvDtUyKfRKt2w3KtffJ41GJUqF6NVNMhs8JLnAY7d813jesz+Zt8cgGpUoFf6sPqAwVbADk0hgvMFjdvSFW6TTe0BkG5VIpLn1MJEzAZ5axhs8wutphXZ6EUJpaqP+whwNbWpsP6IuusNms1h24AFeGtuPrTd4nC2I/aU8vWOrZckoTw/sml9Unl5Qn/dsry4Z9fn9BR+Per8BG9cvzAtyKMUAAAAASUVORK5CYII=""")
        self.ServiceGroupStyleImageFocus = PhotoImage("frameFocusBorder", data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAALKSURBVHhe7Zs7bxNBFIXvjNfGduzEtojiKEQIaGiAngYKkMK/MAV1qOA3QAO0UPAvSEMBFXWgoQAhBVm2ATl2/Ey8D+bM3lg2khEFRbx3Pik60u4o0jk7r8JH1Wq1OhEVzd8ckUrTqHCdhivX6OTcRfK9VU2U8vj1GSfwPb8bZo4PKD/4RLn+R1LRhN/N0UMAR0qpmQAU9VdvUqdyj8JUnnLDz5QZfyPPPzT/xOcxZ5tIeeaDlek4e4nG+aukgyGV2m+ocPQBb+NBhiiK5gMIdZ5+Ve/TOHeZ1g7fUrHzjnQ4soOXlVDnqFe6Td3yHcqOvtL55uupJwRgpnUMzDcv7NrkNg+e0Fp7b+nNA3iAl83vT423CrW2dm0op3AAyn55s8apWn9G6cmP+HGCSJ+0jLfndnnEXpV9bgPAmse0X2+8NOtlYF8kER30ab35yni9Yj3bZ9jtseFhzSfxy/8JZgK8dio7djZoHHXY7bHhSaHYeW88r5hj/gZpnPM46pKw4f0rOhxaz/CuccnBOS8NeIZ3jRseLjnSgGd4t9fbZbnh/U9izylvehGSiguAVSwuAFaxuABYxeICYBWLC4BVLC4AVrG4AFjF4gJgFYsLgFUsLgBWsbgAWMXiAmAViwuAVSwuAFaxuABYxeICYBWLC4BVLC4AVrG4AFjF4gJgFYsJIPDxs3FpxJ4DX6NdhZqMNOAZ3jWqZWhXSQOe4V2jV4dq2WyRKOmgIAbP8K5RKkSvDtUyKfRKt2w3KtffJ41GJUqF6NVNMhs8JLnAY7d813jesz+Zt8cgGpUoFf6sPqAwVbADk0hgvMFjdvSFW6TTe0BkG5VIpLn1MJEzAZ5axhs8wutphXZ6EUJpaqP+whwNbWpsP6IuusNms1h24AFeGtuPrTd4nC2I/aU8vWOrZckoTw/sml9Unl5Qn/dsry4Z9fn9BR+Per8BG9cvzAtyKMUAAAAASUVORK5CYII=""")
        self.ButtonStyleImage = PhotoImage("ButtonBorder", data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAAJjSURBVHhe7Zu9bhNBFIXvzC5Bib2xEgsXKVLTggQSPy+QDhoCnd+DtHkXoKILD8CPRJH0KSNIAbKteO1ECbse5oyvw65xFIkCZffeT7bOzuwWe47XM3eLa7rd7nciSvx3IXncpLPGPTpbuUu/ljYoixJLJoqJDF9xU3D+k2dxnk5uXXyj5dNDWh4fUJSN+PxCUgQwNMb8FUAWr9HJ+haNk4fkTMSz1cK4nBrpV2r19yjOBjz7B+dcavm4RNp6SsebOzRafVRZ8wD3Dg/Hm6+Dp0XMBWCp13lF/Tvb5OwSz1UfZ28HT73OSz8qWy6Nep1tn9hjHtWP0eoT7/EFj6ZcBoBHpM7mZyCE4t8hBIAFb9B+HiYkMGg/C55BCACrfZ3+89eBNQGegcU+j61OGuPkAU2iBlkUOVXe6v4VZ2I6bd73AfgKTyrwblHeSgXebajthQLv/GIjFO/d//o37a3uf2LmCmOBaACsYtEAWMWiAbCKRQNgFYsGwCoWDYBVLBoAq1g0AFaxaACsYtEAWMWiAbCKRQNgFYsGwCoWDYBVLBoAq1g0AFaxaACsYvEBOD6UiPMBuDzjkTy8d4seGx6KA94tGoykAu8W3VVSgXeL1jJ0V0nDuIxWRvtk0VeH1jJpwLPNx9M6AH11ZnIeTkgAXlv9D+E4BICmwrXe+zAhAXidNVJeVoLJyUdqDj/xqL7AI7zOKJXC7R/vah0CvMFjkVIARBN/wRta//m2VmsCvMATvMFjkbkApuAR2Tja9Yl9CdtFVcG9N4efg5fiY1/k2vZ5tJahu6qK7fNhn/db3dVQ+hvJXtCX8Z1Y0gAAAABJRU5ErkJggg==""")

        self.element_create("RoundedFrame", "image", "frameBorder",
        ("focus", "frameFocusBorder"), border=16, sticky="nsew")

        self.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])

        self.element_create("ButtonBorder", "image", "ButtonBorder",
        ("focus", "ButtonBorder"), border=16, sticky="nsew")

        self.layout("RoundedButton", [("RoundedButton", {"sticky": "nsew"})])

        self.configure("TEntry", borderwidth=0,bg="#616161")
