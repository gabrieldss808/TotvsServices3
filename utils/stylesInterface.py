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

        self.configure("TFrame", borderwidth=0,bg="#616161")

    def CreateStyleDynamic(self,GroupNumber=""):
        
        self.element_create("RoundedFrameElement"+GroupNumber, "image", "frameBorder",
        ("focus", "frameFocusBorder"), border=16, sticky="nsew")

        self.layout("RoundedFrame"+GroupNumber, [("RoundedFrameElement"+GroupNumber, {"sticky": "nsew"})])
