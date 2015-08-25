#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Aug 25 22:55:36 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import AISTX
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 326531
        self.offset = offset = 6000
        self.channel_select = channel_select = 1
        self.bit_rate = bit_rate = 9600
        self.RF = RF = 0
        self.IF = IF = 0
        self.BB = BB = 0

        ##################################################
        # Blocks
        ##################################################
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label='offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=-10000,
        	maximum=10000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_offset_sizer)
        _RF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	label='RF',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	minimum=0,
        	maximum=10,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_RF_sizer)
        _IF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._IF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_IF_sizer,
        	value=self.IF,
        	callback=self.set_IF,
        	label='IF',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._IF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_IF_sizer,
        	value=self.IF,
        	callback=self.set_IF,
        	minimum=0,
        	maximum=10,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_IF_sizer)
        _BB_sizer = wx.BoxSizer(wx.VERTICAL)
        self._BB_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_BB_sizer,
        	value=self.BB,
        	callback=self.set_BB,
        	label='BB',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._BB_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_BB_sizer,
        	value=self.BB,
        	callback=self.set_BB,
        	minimum=0,
        	maximum=10,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_BB_sizer)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(162000000 + offset, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(RF, 0)
        self.osmosdr_sink_0.set_if_gain(IF, 0)
        self.osmosdr_sink_0.set_bb_gain(BB, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.digital_gmsk_mod_0_0 = digital.gmsk_mod(
        	samples_per_symbol=int(samp_rate/bit_rate),
        	bt=0.4,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=int(samp_rate/bit_rate),
        	bt=0.4,
        	verbose=False,
        	log=False,
        )
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vcc((0.9, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((0.9, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((0.45, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.45, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=channel_select,
        	output_index=0,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 25000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, -25000, 1, 0)
        self.AISTX_Build_Frame_1 = AISTX.Build_Frame("000001000011101001010100111000100101101111100000000000000001000000011110001101101101001000011110101000110111111001000011010000101111111111001100000000000000000000000000", True, True)
        self.AISTX_Build_Frame_0 = AISTX.Build_Frame("000001000011101001010100111000100101101111100000000000000001000000011110001101101101001000011110101000110111111001000011010000101111111111001100000000000000000000000000", True, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.AISTX_Build_Frame_0, 0), (self.digital_gmsk_mod_0, 0))    
        self.connect((self.AISTX_Build_Frame_1, 0), (self.digital_gmsk_mod_0_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blks2_selector_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_selector_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blks2_selector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blks2_selector_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))    
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.digital_gmsk_mod_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)
        self.osmosdr_sink_0.set_center_freq(162000000 + self.offset, 0)

    def get_channel_select(self):
        return self.channel_select

    def set_channel_select(self, channel_select):
        self.channel_select = channel_select
        self.blks2_selector_0.set_input_index(int(self.channel_select))

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate

    def get_RF(self):
        return self.RF

    def set_RF(self, RF):
        self.RF = RF
        self._RF_slider.set_value(self.RF)
        self._RF_text_box.set_value(self.RF)
        self.osmosdr_sink_0.set_gain(self.RF, 0)

    def get_IF(self):
        return self.IF

    def set_IF(self, IF):
        self.IF = IF
        self._IF_slider.set_value(self.IF)
        self._IF_text_box.set_value(self.IF)
        self.osmosdr_sink_0.set_if_gain(self.IF, 0)

    def get_BB(self):
        return self.BB

    def set_BB(self, BB):
        self.BB = BB
        self._BB_slider.set_value(self.BB)
        self._BB_text_box.set_value(self.BB)
        self.osmosdr_sink_0.set_bb_gain(self.BB, 0)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
