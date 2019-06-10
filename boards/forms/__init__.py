'''
    MicroPY - Textboard/forum written in Python
    Copyright (C) 2019 Kevin Froman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from django import forms

class NewPostForm(forms.Form):
    post_title = forms.CharField(max_length=20)
    reply_to = forms.IntegerField(label='Reply ID')
    post_content = forms.CharField(widget=forms.Textarea)